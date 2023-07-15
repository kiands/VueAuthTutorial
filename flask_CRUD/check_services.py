from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import json
import mysql.connector
import os

# load .env file
with open('../.env') as file:
    for line in file:
        key, value = line.strip().split('=', 1)
        os.environ[key] = value

# read environment parameters
database_passwd = os.environ.get("DATABASE_PASSWORD")

# 数据库配置
config = {
    "host": "localhost",        # 数据库地址
    "user": "root",    # 数据库用户名
    "passwd": database_passwd,  # 数据库密码
    "database": "FaceFriendsFoundation"  # 数据库名称
}

check_services_blueprint = Blueprint('check_services', __name__)

# 测试服务项目API的路由
@check_services_blueprint.route('/api/cms/services', methods=['GET'])
def contacts():
    sql_detect = """
        select count(booking_id) from booked_services
    """
    sql_read = """
        select booked_services.*, users.email
        from booked_services
        join users on booked_services.user_id = users.user_id
        where booked_services.status != 0
        order by booking_id limit 10
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_detect)
    count = cursor.fetchall()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    services = []
    for i in range(0, len(result)):
        services.append({
            'booking_id' : result[i][0],
            'user_id' : result[i][1],
            'service_name' : result[i][2],
            'date' : result[i][3],
            'time' : result[i][4],
            'status' : result[i][5],
            'message': result[i][6],
            'user_email' : result[i][7]
        })
    return jsonify({
        'count': count[0][0],
        'services': services
    })