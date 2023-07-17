from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from datetime import timedelta
# 导入路由文件并在后面注册蓝图或是需要用到的变量，如auth中的revoked_tokens（装载已撤销JWT的list）
from auth import auth_blueprint, revoked_tokens
from services import services_blueprint
from manage_home import manage_home_blueprint
from manage_contacts import manage_contacts_blueprint
from manage_services import manage_services_blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'  # 需要替换成随机的字符串
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=15)  # 设置访问令牌有效期为15分钟
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(days=7)  # 设置刷新令牌有效期为7天
# 注册不同功能模块的蓝图
app.register_blueprint(auth_blueprint)
app.register_blueprint(services_blueprint)
app.register_blueprint(manage_home_blueprint)
app.register_blueprint(manage_contacts_blueprint)
app.register_blueprint(manage_services_blueprint)
# CORS(app, resources={r"/api/*": {"origins": "*"}})
CORS(app, resources={r"/api/*": {"origins": "*", "allow_headers": "*"}})

# 创建 JWTManager 对象（这个只能在app层级上实例化，无法在Blueprint层级上进行，所以只能在app.py中操作）
jwt = JWTManager(app)

# 检查 JWT token 是否被吊销的回调函数
# 通过 jwt.token_in_blocklist_loader 装饰器将 check_if_token_revoked()注册到 JWTManager 中
@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return jti in revoked_tokens

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
