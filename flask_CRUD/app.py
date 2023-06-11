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
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 需要替换成随机的字符串
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)  # 设置访问令牌有效期为15分钟
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)  # 设置刷新令牌有效期为7天
jwt = JWTManager(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# load .env file
with open('../.env') as file:
    for line in file:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

# read environment parameters
database_passwd = os.environ.get("DATABASE_PASSWORD")
google_oauth_id = os.environ.get("GOOGLE_OAUTH_ID")
google_oauth_secret = os.environ.get("GOOGLE_OAUTH_SECRET")
google_oauth_redirect_uri = os.environ.get("GOOGLE_OAUTH_REDIRECT_URI")
google_oauth_token_uri = os.environ.get("GOOGLE_OAUTH_TOKEN_URI")
google_userinfo_uri = os.environ.get("GOOGLE_USER_INFO_URI")

# 数据库配置
config = {
    "host": "localhost",        # 数据库地址
    "user": "root",    # 数据库用户名
    "passwd": database_passwd,  # 数据库密码
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

# Google OAuth API
@app.route('/api/google/oauth', methods=['GET'])
def google_oauth_login():
    # connect to MySQL
    conn = mysql.connector.connect(**config)
    # create a cursor
    cursor = conn.cursor()
    # get code from google
    code = request.args.get('code')
    params = {
        'code': code,
        'client_id': google_oauth_id,
        'client_secret': google_oauth_secret,
        'redirect_uri': google_oauth_redirect_uri,
        'grant_type': 'authorization_code'
    }
    # post necessary data to google to fetch user data
    # At the first time I wrongly thought I should use a redirect route.
    # But the next lines will bring back necessary data.
    response = requests.post(google_oauth_token_uri, data=params)
    token_response = response.json()
    # Finally we can load the access token that allows the website to access user's Google information.
    access_token = token_response.get('access_token')
    # Get user information
    front_end_request_header = {'Authorization': f'Bearer {access_token}'}
    google_user_info_response = requests.get(google_userinfo_uri, headers=front_end_request_header)
    # Sometimes user_data['name'] is not set so we can use user_data['login'] instead
    # logic for creating a new user or logging an existed user
    if google_user_info_response.status_code == 200:
        user_data = google_user_info_response.json()
        # SQLs
        sql_create = """
            INSERT INTO users (nickname, email, password, created_at)
            VALUES (%s, %s, %s, %s)
        """

        sql_read = """
            SELECT * FROM users
            WHERE email = %s
        """

        # check if this user exists
        cursor.execute(sql_read, (user_data['email'],))
        result = cursor.fetchall()
        # Don't close the cursor and the connection here.

        # if the user's email already exists
        if result:
            user_id = result[0][0]
            nickname = result[0][1]
            # Generate a JWT token for the user
            jwt_token = create_access_token(identity=user_id)
            # Generate a Refresh token for the user
            refresh_token = create_refresh_token(identity=user_id)
            # This should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
            # close the cursor and connection
            cursor.close()
            conn.close()
            return render_template('success.html', user_id = user_id, user_name = nickname, access_token = jwt_token, refresh_token = refresh_token)
        # else, a new user
        else:
            # data to process
            nickname = user_data['name']
            email = user_data['email']
            # for OAuth, generate a randomized password at 8 digits
            password = secrets.token_urlsafe(8)
            # generate a randomized salt
            salt = secrets.token_bytes(8)
            # combine the password and salt and then hash it
            salted_password = salt + password.encode()
            hashed_password = hashlib.sha256(salted_password).hexdigest()
            print(len(hashed_password))
            created_at = datetime.now()
            # execute the insertion
            cursor.execute(sql_create, (nickname, email, hashed_password, created_at))
            # commit the changes to database
            conn.commit()

            # after creating, check the new user's user_id because we need to identify our users
            cursor.execute(sql_read, (email,))
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
    sql_read = """
        select service_name,service_description from services
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    services = []
    service_descriptions = {}
    for i in range(0, len(result)):
        services.append(result[i][0])
        service_descriptions[result[i][0]] = result[i][1]
    return jsonify({
        'services': services,
        'service_descriptions': service_descriptions
    })

# 测试服务项目允许的时间段API的路由
@app.route('/api/service_time_slots', methods=['POST'])
@jwt_required()
def currentAllowedDates():
    data = request.get_json()
    service = data['service']
    sql_read = """
        SELECT time_slots FROM services
        WHERE service_name = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (service,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({ 'timeSlots': json.loads(result[0][0]) })

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data['name']
    email = data['email']
    source = data['source']
    reason = data['reason']
    additional_information = data['additional_information']
    sql_create = """
        INSERT INTO contacts (name, email, source, reason, additional_information)
        VALUES (%s, %s, %s, %s, %s)
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_create, (name, email, source, reason, additional_information,))
    # For insert into, we need to commit it.
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"msg": "Received"}), 200

# This function has an atomic or consistency problem. Not serious if the current is small. Need ti be discussed.
@app.route('/api/book_service', methods=['POST'])
def bookService():
    data = request.get_json()
    user_id = data['user_id']
    service_name = data['service_name']
    date = data['date']
    time = data['time']
    sql_read = """
        select time_slots from services
        where service_name = %s
    """
    json_path = '$."{}"."{}"'.format(date, time)
    sql_update = """
        UPDATE services
        SET time_slots = JSON_SET(time_slots, %s, %s)
        WHERE service_name = %s
    """
    sql_create = """
        INSERT INTO booked_services (user_id, service_name, date, time)
        VALUES (%s, %s, %s, %s)
    """

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (service_name,))
    result = cursor.fetchall()
    remaining = json.loads(result[0][0])[date][time]
    if remaining >= 1:
        # Update the database and return modified `timeSlots` directly because they just look the same.
        cursor.execute(sql_update, (json_path, remaining - 1, service_name))
        conn.commit()
        new_result = json.loads(result[0][0])
        # This mutation is inplace
        new_result[date][time] = remaining - 1
        # Then insert a new record into booked_services
        cursor.execute(sql_create, (user_id, service_name, date, time,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({ "timeSlots": new_result })
    else:
        # When the newest `timeSlots` is unavailable, return the newest query result directly to force an update.
        cursor.close()
        conn.close()
        return jsonify({ "timeSlots": json.loads(result[0][0]) })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)