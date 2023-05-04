from flask import Flask, jsonify, request, render_template, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 需要替换成随机的字符串
jwt = JWTManager(app)
CORS(app)

users = []

@app.route('/api/test', methods=['GET'])
# Decorater for jwt requirement, MUST PLACE @jwt_required() CLOSE TO FUNCTION
@jwt_required()
def test():
    return "1"

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
    jwt_token = create_access_token(identity="user_name")
    return jsonify({'user_name': user_name, 'access_token': jwt_token})

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
        # Don't know what's it for
        session['user'] = user
        print(user['user_name'])
        return jsonify({'user_name': user['user_name'], 'access_token': jwt_token})
    else:
        return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return '', 204

@app.route('/api/user', methods=['GET'])
def get_user():
    user = session.get('user', None)
    if user:
        return jsonify(user)
    else:
        return jsonify({'error': 'Not logged in'}), 401

@app.route('/api/github/auth', methods=['GET'])
def oauth_login():
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
    if user_info_response.status_code == 200:
        user_data = user_info_response.json()
        # Generate a JWT token for the user
        jwt_token = create_access_token(identity=user_data['login'])
        # this should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
        return render_template('success.html', user_name = user_data['login'], access_token = jwt_token)
    else:
        return jsonify({'error': 'No such user'}), 401

if __name__ == '__main__':
    app.run(port=8000, debug=True)
