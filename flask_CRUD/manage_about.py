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

manage_about_blueprint = Blueprint('manage_about', __name__)

# 读取项目
@manage_about_blueprint.route('/api/cms/programs', methods=['GET'])
def programs():
    sql_read = """
        select * from programs
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    programs = []
    for i in range(0, len(result)):
        programs.append({
            'program_id' : result[i][0],
            'source' : result[i][1],
            'link' : result[i][2],
            'title' : result[i][3],
            'content' : result[i][4]
        })
    return jsonify({
        'programs': programs
    })

# 更新项目
@manage_about_blueprint.route('/api/cms/programs/<int:program_id>', methods=['PUT'])
@jwt_required()
def update_program(program_id):
    sql_update = """
        update programs
        set source = %s, link = %s, title = %s, content = %s
        where program_id = %s
    """
    data = request.get_json()
    src = data.get('src')
    link = data.get('link')
    title = data.get('title')
    content = data.get('content')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_update, (src, link, title, content, program_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Program updated successfully!'})

# 新增项目
@manage_about_blueprint.route('/api/cms/programs', methods=['POST'])
@jwt_required()
def create_program():
    sql_create = """
        insert into programs (source, link, title, content)
        values (%s, %s, %s, %s)
    """
    data = request.get_json()
    src = data.get('src')
    link = data.get('link')
    title = data.get('title')
    content = data.get('content')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_create, (src, link, title, content))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Program created successfully!'})

# 删除项目
@manage_about_blueprint.route('/api/cms/programs/<int:program_id>', methods=['DELETE'])
@jwt_required()
def delete_carousel(program_id):
    sql_delete = """
        DELETE FROM programs WHERE program_id = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_delete, (program_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Program deleted successfully!'})