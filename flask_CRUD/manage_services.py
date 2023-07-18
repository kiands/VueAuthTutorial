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
@manage_services_blueprint.route('/api/cms/services', methods=['GET'])
def check_services():
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

# 撤销服务预订
@manage_services_blueprint.route('/api/cms/revoke_booking', methods=['POST'])
def revoke_booking():
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
    sql_update_services = """
        UPDATE services
        SET time_slots = JSON_SET(time_slots, %s, %s)
        WHERE service_name = %s
    """
    sql_update_booking = """
        UPDATE booked_services
        SET status = -1
        WHERE service_name = %s and (status = %s or status = %s)
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
    cursor.execute(sql_update_booking, (service_name, 0, 1,))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({ "timeSlots": new_result, "bookedService": { 'service_name': '' } })