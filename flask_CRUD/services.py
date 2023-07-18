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

services_blueprint = Blueprint('services', __name__)

# 测试服务项目API的路由
@services_blueprint.route('/api/services', methods=['GET'])
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
@services_blueprint.route('/api/service_time_slots', methods=['POST'])
@jwt_required()
def currentAllowedDates():
    data = request.get_json()
    service_name = data['service_name']
    sql_read = """
        SELECT time_slots FROM services
        WHERE service_name = %s
    """
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (service_name,))
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify({ 'timeSlots': json.loads(result[0][0]) })

@services_blueprint.route('/api/contact', methods=['POST'])
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

# This function is used to fetch and check current user's booked service, also called pending/approved service
@services_blueprint.route('/api/booked_service', methods=['POST'])
@jwt_required()
def bookedService():
    data = request.get_json()
    user_id = data['user_id']
    service_name = data['service_name']
    sql_read = """
        select * from booked_services
        where user_id = %s and (status = %s or status = %s) and service_name = %s
    """

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_read, (user_id, 0, 1, service_name,))
    result = cursor.fetchall()
    # Not null.
    if len(result) != 0:
        cursor.close()
        conn.close()
        print(result[-1])
        return jsonify({ "bookedService": { 'booking_id': result[-1][0], 'service_name': result[-1][2], 'date': result[-1][3], 'time': result[-1][4] } })
    # Null.
    else:
        cursor.close()
        conn.close()
        return jsonify({ "bookedService": { 'service_name': '' } })

# This function has an atomic or consistency problem. Not serious if the current is small. Need ti be discussed.
@services_blueprint.route('/api/book_service', methods=['POST'])
@jwt_required()
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
        return jsonify({ "timeSlots": json.loads(result[0][0]), "bookedService": { 'service_name': '' } })

# This function has an atomic or consistency problem. Not serious if the current is small. Need ti be discussed.
@services_blueprint.route('/api/cancel_booking', methods=['POST'])
@jwt_required()
def cancelBooking():
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
    return jsonify({ "timeSlots": new_result, "bookedService": { 'service_name': '' } })