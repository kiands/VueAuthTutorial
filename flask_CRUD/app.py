from flask import Flask, jsonify, request, render_template, session
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import requests
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 需要替换成随机的字符串
CORS(app)

users = []

@app.route('/test', methods=['GET'])
def test():
    return "1"

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    print(data)
    username = data['username']
    email = data['email']
    password = data['password']
    hashed_password = generate_password_hash(password)
    user = {'username': username, 'email': email, 'password': hashed_password}
    users.append(user)
    session['user'] = user
    # temporarily use fixed token
    # return jsonify(user)
    return jsonify({'username': "1", 'token': 'token'})

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    print(data)
    email = data['email']
    password = data['password']
    user = next((u for u in users if u['email'] == email), None)
    if user and check_password_hash(user['password'], password):
        session['user'] = user
        return jsonify(user)
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
    # Finally we can load access_token
    access_token = json.loads(response.text).get('access_token')
    # this should cooperate with window.open to oauth provider at front end, shouldn't be a <a> tag
    return render_template('success.html', access_token = access_token, user_name = 'test')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
