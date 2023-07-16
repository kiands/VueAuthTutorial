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

manage_home_blueprint = Blueprint('manage_home', __name__)

# 读取轮播图
@manage_home_blueprint.route('/api/cms/carousels', methods=['GET'])
def carousels():
    sql_read = """
        select * from carousels
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    carousels = []
    for i in range(0, len(result)):
        carousels.append({
            'carousel_id' : result[i][0],
            'source' : result[i][1],
            'link' : result[i][2],
            'name' : result[i][3],
            'description' : result[i][4]
        })
    return jsonify({
        'carousels': carousels
    })

# 更新轮播图
@manage_home_blueprint.route('/api/cms/carousels/<int:carousel_id>', methods=['PUT'])
def update_carousel(carousel_id):
    sql_update = """
        update carousels
        set source = %s, link = %s
        where carousel_id = %s
    """
    data = request.get_json()
    src = data.get('src')
    link = data.get('link')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_update, (src, link, carousel_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Carousel updated successfully!'})