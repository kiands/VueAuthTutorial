from flask import Flask, jsonify, request, render_template, session
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, create_refresh_token, get_jwt_identity, get_jwt
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json
import mysql.connector
from datetime import datetime, timedelta
import secrets
import hashlib

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 需要替换成随机的字符串
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=1)  # 设置访问令牌有效期为15分钟
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=30)  # 设置刷新令牌有效期为30天
jwt = JWTManager(app)
CORS(app)

# 数据库配置
config = {
    "host": "localhost",        # 数据库地址
    "user": "root",    # 数据库用户名
    "passwd": "HZFmysql2023",  # 数据库密码
    "database": "FaceFriendsFoundation"  # 数据库名称
}

# 简单的用于临时代替数据库的数组
users = []
# Revoked JWT tokens
revoked_tokens = []

# 检查JWT token是否被吊销的回调函数。@jwt_required会用这个来检查请求中的JWT token是否被吊销并加以应对
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in revoked_tokens

# 用于刷新JWT token的端点
@app.route("/api/refresh_token", methods=["POST"])
# 通过设置refresh=True，这个装饰器会要求提供一个有效的刷新令牌
@jwt_required(refresh=True)
def refresh_token():
    current_user = get_jwt_identity()
    new_access_token = create_access_token(identity=current_user)
    return jsonify(access_token=new_access_token)

# 注册用的API
@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    user_name = data['user_name']
    email = data['email']
    password = data['password']
    hashed_password = generate_password_hash(password)
    user = {'user_name': user_name, 'email': email, 'password': hashed_password}
    users.append(user)
    session['user'] = user
    # Generate a JWT token for the user
    jwt_token = create_access_token(identity=user_name)
    # Generate a Refresh token for the user
    refresh_token = create_refresh_token(identity=user_name)
    return jsonify({'user_name': user_name, 'access_token': jwt_token, 'refresh_token': refresh_token})

# 登陆用的API
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']
    user = next((u for u in users if u['email'] == email), None)
    if user and check_password_hash(user['password'], password):
        # Generate a JWT token for the user
        jwt_token = create_access_token(identity=user['user_name'])
        # Generate a Refresh token for the user
        refresh_token = create_refresh_token(identity=user['user_name'])
        # Don't know what's it for
        session['user'] = user
        print(user['user_name'])
        return jsonify({'user_name': user['user_name'], 'access_token': jwt_token, 'refresh_token': refresh_token})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

# GitHub OAuth API
@app.route('/api/github/auth', methods=['GET'])
def github_oauth_login():
    # connect to MySQL
    conn = mysql.connector.connect(**config)
    # create a cursor
    cursor = conn.cursor()
    # get code from github
    args = request.args
    code = args.get("code")
    # post necessary data to github to fetch user data
    oauth_token_url = 'https://github.com/login/oauth/access_token'
    oauth_token_request_payload = {
        'client_id': '89450a7c608bbd0300d8',
        'client_secret': 'cd2dbe4225c7020faa78b72e2126f430848d1360',
        'code': code
    }
    # At the first time I wrongly thought I should use a redirect route.
    # But the next lines will bring back necessary data.
    response = requests.post(
        oauth_token_url,
        data = oauth_token_request_payload,
        headers = {'Accept': 'application/json'}
    )
    # Finally we can load the access token that allows the website to access user's GitHub information.
    access_token = json.loads(response.text).get('access_token')
    # Get user information
    front_end_request_header = {'Authorization': f'Bearer {access_token}'}
    user_info_response = requests.get('https://api.github.com/user', headers=front_end_request_header)
    # Sometimes user_data['name'] is not set so we can use user_data['login'] instead
    # logic for creating a new user or logging an existed user
    if user_info_response.status_code == 200:
        user_data = user_info_response.json()
        # SQLs
        sql_create = """
            INSERT INTO users (nickname, email, password, created_at)
            VALUES (%s, %s, %s, %s)
        """

        sql_read = """
            SELECT * FROM users
            WHERE nickname = %s
        """

        # check if this user exists
        cursor.execute(sql_read, (user_data['login'],))
        result = cursor.fetchall()

        if result:
            user_id = result[0][0]
            nickname = result[0][1]
            # Generate a JWT token for the user
            jwt_token = create_access_token(identity=user_id)
            # Generate a Refresh token for the user
            refresh_token = create_refresh_token(identity=user_id)
            # This should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
            return render_template('success.html', user_id = user_id, user_name = nickname, access_token = jwt_token, refresh_token = refresh_token)
        else:
            # data to process
            nickname = user_data['login']
            if user_data['email'] == None:
                email = "no@no.com"
            else:
                email = user_data['email']
            # for OAuth, generate a randomized password at 10 digits
            password = secrets.token_urlsafe(10)
            # generate a randomized salt
            salt = secrets.token_bytes(16)
            # combine the password and salt and then hash it
            salted_password = salt + password.encode()
            hashed_password = hashlib.sha256(salted_password).hexdigest()
            created_at = datetime.now()
            # execute the insertion
            cursor.execute(sql_create, (nickname, email, hashed_password, created_at))
            # commit the changes to database
            conn.commit()

            # after creating, check the new user's user_id because we need to identify our users
            cursor.execute(sql_read, (nickname,))
            user_id = cursor.fetchall()[0][0]
            # close the cursor and connection
            cursor.close()
            conn.close()

            # Generate a JWT token for the user
            jwt_token = create_access_token(identity=user_id)
            # Generate a Refresh token for the user
            refresh_token = create_refresh_token(identity=user_id)
            # This should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
            return render_template('success.html', user_id = user_id, user_name = nickname, access_token = jwt_token, refresh_token = refresh_token)
    else:
        return jsonify({'error': 'No such user'}), 401

# 获取用户信息的API
@app.route('/api/user', methods=['GET'])
def get_user():
    user = session.get('user', None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Not logged in'}), 401

# 测试用的API
@app.route('/api/test', methods=['GET'])
# Decorater for jwt requirement, MUST PLACE @jwt_required() CLOSE TO FUNCTION
@jwt_required()
def test():
    return "1"

# 登出
@app.route('/api/logout', methods=['POST'])
@jwt_required()
def logout():
    jti = get_jwt()["jti"]  # 获取令牌的唯一标识（JTI）
    revoked_tokens.append(jti)
    session.pop('user', None)
    return jsonify({"msg": "Logged out and current JWT token is revoked"}), 204

# 测试服务项目API的路由
@app.route('/api/services', methods=['GET'])
def services():
    return jsonify({
        'services': ['PYFS', 'PYTS'],
        'servicesBody': {
            "PYFS": { "title": "PYFS" },
            "PYTS": { "title": "PYTS" }
        }
    })

# 测试服务项目允许的时间段API的路由
@app.route('/api/service-current-allowed-dates', methods=['POST'])
def currentAllowedDates():
    data = request.get_json()
    service = data['service']
    if service == 'PYFS':
        response = ['2023-06-08', '2023-06-09', '2023-06-19', '2023-06-20', '2023-06-21']
    else:
        response = ['2023-06-06', '2023-06-07', '2023-06-08']
    return jsonify({ 'currentAllowedDates': response })

if __name__ == '__main__':
    app.run(port=8000, debug=True)