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

check_contacts_blueprint = Blueprint('check_contacts', __name__)

# 测试服务项目API的路由
@check_contacts_blueprint.route('/api/contacts', methods=['GET'])
def contacts():
    sql_detect = """
        select count(contact_id) from contacts
    """
    sql_read = """
        select * from contacts order by contact_id limit 10
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_detect)
    count = cursor.fetchall()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    contacts = []
    for i in range(0, len(result)):
        contacts.append({
            'contact_id' : result[i][0],
            'name' : result[i][1],
            'email' : result[i][2],
            'source' : result[i][3],
            'reason' : result[i][4],
            'additional_information' : result[i][5]
        })
    return jsonify({
        'count': count[0][0],
        'contacts': contacts
    })