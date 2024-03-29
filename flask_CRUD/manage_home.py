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
        select * from homepage_images
        where type = 'carousel'
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
            'image_id' : result[i][0],
            'type': result[i][1],
            'source' : result[i][2],
            'link' : result[i][3],
            'name' : result[i][4],
            'description' : result[i][5]
        })
    return jsonify({
        'carousels': carousels
    })

# 更新轮播图
@manage_home_blueprint.route('/api/cms/carousels/<int:carousel_id>', methods=['PUT'])
@jwt_required()
def update_carousel(carousel_id):
    sql_update = """
        update homepage_images
        set source = %s, link = %s
        where image_id = %s
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

# 新增轮播图
@manage_home_blueprint.route('/api/cms/carousels', methods=['POST'])
@jwt_required()
def create_carousel():
    sql_create = """
        insert into homepage_images (type, source, link)
        values (%s, %s, %s)
    """
    data = request.get_json()
    type = 'carousel'
    src = data.get('src')
    link = data.get('link')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_create, (type, src, link,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Carousel created successfully!'})

# 删除轮播图
@manage_home_blueprint.route('/api/cms/carousels/<int:carousel_id>', methods=['DELETE'])
@jwt_required()
def delete_carousel(carousel_id):
    sql_delete = """
        DELETE FROM homepage_images WHERE image_id = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_delete, (carousel_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Carousel deleted successfully!'})

# 读取海报
@manage_home_blueprint.route('/api/cms/flyers', methods=['GET'])
@jwt_required()
def flyers():
    sql_read = """
        select * from homepage_images
        where type = 'flyer'
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    flyers = []
    for i in range(0, len(result)):
        flyers.append({
            'image_id' : result[i][0],
            'type': result[i][1],
            'source' : result[i][2],
            'link' : result[i][3],
            'name' : result[i][4],
            'description' : result[i][5]
        })
    return jsonify({
        'flyers': flyers
    })

# 更新海报
@manage_home_blueprint.route('/api/cms/flyers/<int:flyer_id>', methods=['PUT'])
@jwt_required()
def update_flyer(flyer_id):
    sql_update = """
        update homepage_images
        set source = %s, link = %s
        where image_id = %s
    """
    data = request.get_json()
    src = data.get('src')
    link = data.get('link')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_update, (src, link, flyer_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Flyer updated successfully!'})

# 读取赞助商
@manage_home_blueprint.route('/api/cms/sponsors', methods=['GET'])
def sponsors():
    sql_read = """
        select * from homepage_images
        where type = 'sponsor'
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    sponsors = []
    for i in range(0, len(result)):
        sponsors.append({
            'image_id' : result[i][0],
            'type': result[i][1],
            'source' : result[i][2],
            'link' : result[i][3],
            'name' : result[i][4],
            'description' : result[i][5]
        })
    return jsonify({
        'sponsors': sponsors
    })

# 更新赞助商
@manage_home_blueprint.route('/api/cms/sponsors/<int:sponsor_id>', methods=['PUT'])
@jwt_required()
def update_sponsors(sponsor_id):
    sql_update = """
        update homepage_images
        set source = %s, link = %s
        where image_id = %s
    """
    data = request.get_json()
    src = data.get('src')
    link = data.get('link')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_update, (src, link, sponsor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Sponsor updated successfully!'})

# 新增赞助商
@manage_home_blueprint.route('/api/cms/sponsors', methods=['POST'])
@jwt_required()
def create_sponsor():
    sql_create = """
        insert into homepage_images (type, source, link)
        values (%s, %s, %s)
    """
    data = request.get_json()
    type = 'sponsor'
    src = data.get('src')
    link = data.get('link')
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_create, (type, src, link,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Sponsor created successfully!'})

# 删除赞助商
@manage_home_blueprint.route('/api/cms/sponsors/<int:sponsor_id>', methods=['DELETE'])
@jwt_required()
def delete_sponsor(sponsor_id):
    sql_delete = """
        DELETE FROM homepage_images WHERE image_id = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_delete, (sponsor_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'message': 'Sponsor deleted successfully!'})