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

manage_services_blueprint = Blueprint('manage_services', __name__)

# 查看当前服务预订列表
@manage_services_blueprint.route('/api/cms/booked_services', methods=['GET'])
def check_booked_services():
    sql_detect = """
        select count(booking_id) from booked_services where status != -1
    """
    sql_read = """
        select booked_services.*, users.email
        from booked_services
        join users on booked_services.user_id = users.user_id
        where booked_services.status != -1
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

# 撤销服务预订
@manage_services_blueprint.route('/api/cms/revoke_booking', methods=['POST'])
def revoke_booking():
    data = request.get_json()
    booking_id = data['booking_id']
    service_name = data['service_name']
    date = data['date']
    time = data['time']
    sql_read = """
        select time_slots from services
        where service_name = %s
    """
    json_path = '$."{}"."{}"'.format(date, time)
    sql_update_services = """
        UPDATE services
        SET time_slots = JSON_SET(time_slots, %s, %s)
        WHERE service_name = %s
    """
    sql_update_booking = """
        UPDATE booked_services
        SET status = -1
        WHERE booking_id = %s
    """

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (service_name,))
    result = cursor.fetchall()
    remaining = json.loads(result[0][0])[date][time]
    # Update the database and return modified `timeSlots` directly because they just look the same.
    cursor.execute(sql_update_services, (json_path, remaining + 1, service_name))
    conn.commit()
    new_result = json.loads(result[0][0])
    # This mutation is inplace
    new_result[date][time] = remaining + 1
    # Then update the booking record
    cursor.execute(sql_update_booking, (booking_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify("Revoked successfully!")

# 查看当前提供的服务
@manage_services_blueprint.route('/api/cms/services', methods=['GET'])
def check_services():
    sql_read = """
        select * from services
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    services = []
    for i in range(0, len(result)):
        services.append({
            'service_id': result[i][0],
            'service_name': result[i][1],
            'service_description': result[i][2],
            'time_slots': result[i][3]
        })
    return jsonify({
        'services': services
    })

# 添加新服务
@manage_services_blueprint.route('/api/cms/services', methods=['POST'])
def add_new_service():
    data = request.get_json()
    service_name = data['service_name']
    service_description = data['service_description']
    sql_create = """
        INSERT INTO services (service_name, service_description, time_slots)
        VALUES (%s, %s, %s)
    """
    empty_time_slots = {}
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_create, (service_name, service_description, json.dumps(empty_time_slots)))
    conn.commit()
    cursor.close()
    conn.close()
    return "Success!"

# 删除服务
# `DELETE` seems not support payload?
@manage_services_blueprint.route('/api/cms/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    sql_delete = """
        DELETE FROM services WHERE service_id = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_delete, (service_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return "Success!"

# 更新服务的time slots
@manage_services_blueprint.route('/api/cms/services', methods=['PUT'])
# @jwt_required()
def update_service():
    data = request.get_json()
    service_name = data['service_name']
    # New time slots.
    new_time_slots = data['new_time_slots']
    sql_read = """
        select time_slots from services
        where service_name = %s
    """
    sql_update = """
        UPDATE services
        SET time_slots = %s
        WHERE service_name = %s
    """

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (service_name,))
    result = cursor.fetchall()
    slots = json.loads(result[0][0])
    # Dict has 'update()'.
    slots.update(new_time_slots)
    cursor.execute(sql_update, (json.dumps(slots), service_name))
    conn.commit()
    cursor.close()
    conn.close()
    return "Success!"