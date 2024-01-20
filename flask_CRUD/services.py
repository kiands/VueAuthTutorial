from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
import json
import mysql.connector
import redis
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

# connect to redis
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

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
# def bookedService():
#     data = request.get_json()
#     user_id = data['user_id']
#     service_name = data['service_name']
#     sql_read = """
#         select * from booked_services
#         where user_id = %s and (status = %s or status = %s) and service_name = %s
#     """

#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute(sql_read, (user_id, 0, 1, service_name,))
#     result = cursor.fetchall()
#     # Not null.
#     if len(result) != 0:
#         cursor.close()
#         conn.close()
#         print(result[-1])
#         return jsonify({ "bookedService": { 'booking_id': result[-1][0], 'service_name': result[-1][2], 'date': result[-1][3], 'time': result[-1][4] } })
#     # Null.
#     else:
#         cursor.close()
#         conn.close()
#         return jsonify({ "bookedService": { 'service_name': '' } })
def bookedService():
    data = request.get_json()
    user_id = data['user_id']
    service_name = data['service_name']

    # 构建 Redis 键
    redis_key = f"booked_service:{user_id}:{service_name}"

    # 尝试从 Redis 获取预订信息
    booked_service = redis_client.get(redis_key)
    if booked_service:
        booked_service_data = json.loads(booked_service)
        # 检查是否有有效的预订信息
        if booked_service_data.get("service_name"):
            print("cache")
            print(booked_service)
            return jsonify({"bookedService": booked_service_data})
        else:
            # 通过埋点打印状态，解决了redis会主动创建空key-value对导致永远不会参考数据库的情况发生
            print("mysql")
            # 从数据库获取预订信息
            booked_service = fetch_and_cache_booked_service(user_id, service_name, redis_key)
            return jsonify({"bookedService": booked_service})
    else:
        print("mysql")
        # 从数据库获取预订信息
        booked_service = fetch_and_cache_booked_service(user_id, service_name, redis_key)
        return jsonify({"bookedService": booked_service})

def fetch_and_cache_booked_service(user_id, service_name, redis_key):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    sql_read = """
        SELECT * FROM booked_services
        WHERE user_id = %s AND (status = %s OR status = %s) AND service_name = %s
    """
    cursor.execute(sql_read, (user_id, 0, 1, service_name,))
    result = cursor.fetchall()
    conn.close()

    # 如果找到预订信息，更新Redis并返回
    if len(result) != 0:
        booked_data = {
            'booking_id': result[-1][0], 
            'service_name': result[-1][2], 
            'date': result[-1][3], 
            'time': result[-1][4]
        }
        # 设置预订记录的redis key-value对
        redis_client.set(redis_key, json.dumps(booked_data))
        return booked_data
    else:
        # 如果没有找到预订信息，返回空的预订信息
        empty_data = {'service_name': ''}
        redis_client.set(redis_key, json.dumps(empty_data))
        return empty_data

# This function has an atomic or consistency problem. Not serious if the current is small. Need ti be discussed.
@services_blueprint.route('/api/book_service', methods=['POST'])
@jwt_required()
# def bookService():
#     data = request.get_json()
#     user_id = data['user_id']
#     service_name = data['service_name']
#     date = data['date']
#     time = data['time']
#     sql_read = """
#         select time_slots from services
#         where service_name = %s
#     """
#     json_path = '$."{}"."{}"'.format(date, time)
#     sql_update = """
#         UPDATE services
#         SET time_slots = JSON_SET(time_slots, %s, %s)
#         WHERE service_name = %s
#     """
#     sql_create = """
#         INSERT INTO booked_services (user_id, service_name, date, time)
#         VALUES (%s, %s, %s, %s)
#     """

#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute(sql_read, (service_name,))
#     result = cursor.fetchall()
#     remaining = json.loads(result[0][0])[date][time]
#     if remaining >= 1:
#         # Update the database and return modified `timeSlots` directly because they just look the same.
#         cursor.execute(sql_update, (json_path, remaining - 1, service_name))
#         conn.commit()
#         new_result = json.loads(result[0][0])
#         # This mutation is inplace
#         new_result[date][time] = remaining - 1
#         # Then insert a new record into booked_services
#         cursor.execute(sql_create, (user_id, service_name, date, time,))
#         conn.commit()
#         cursor.close()
#         conn.close()
#         # Return new time slots here and the newest booked service can be handled by requesting route: booked_service.
#         # Maybe it is not a good idea to compute new time slot (new_result) inplacely. We should use a route to request the new time slot when booking is busy.
#         return jsonify({ "timeSlots": new_result })
#     else:
#         # When the newest `timeSlots` is unavailable, return the newest query result directly to force an update.
#         cursor.close()
#         conn.close()
#         return jsonify({ "timeSlots": json.loads(result[0][0]), "bookedService": { 'service_name': '' } })
def bookService():
    data = request.get_json()
    user_id = data['user_id']
    service_name = data['service_name']
    date = data['date']
    time = data['time']

    # Redis键的构建
    redis_key = f"service_slots:{service_name}:{date}"

    # 从Redis获取时间槽信息
    time_slots = redis_client.get(redis_key)
    if time_slots:
        time_slots = json.loads(time_slots)
    else:
        # 如果Redis中没有，则从数据库读取并更新Redis
        time_slots = load_and_cache_time_slots_for_booking(service_name, redis_key)

    # 检查时间槽是否可用
    remaining = int(time_slots.get(date, {}).get(time, 0))
    if remaining >= 1:
        try:
            # 更新数据库
            update_database(service_name, date, time, remaining, user_id)

            # 更新Redis
            time_slots[date][time] = remaining - 1
            redis_client.set(redis_key, json.dumps(time_slots))
        except Exception as e:
            # 如果数据库更新失败，则不更新缓存，并将错误返回给用户
            return jsonify({"error": str(e)}), 500

        return jsonify({"timeSlots": time_slots})
    else:
        # 时间槽不可用，返回最新的时间槽信息
        return jsonify({"timeSlots": time_slots, "bookedService": {'service_name': ''}})

def load_and_cache_time_slots_for_booking(service_name, redis_key):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    sql_read = """
        SELECT time_slots FROM services
        WHERE service_name = %s
    """
    cursor.execute(sql_read, (service_name,))
    result = cursor.fetchall()
    conn.close()

    time_slots = json.loads(result[0][0])
    redis_client.set(redis_key, json.dumps(time_slots))
    return time_slots

def update_database(service_name, date, time, remaining, user_id):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    json_path = '$."{}"."{}"'.format(date, time)
    sql_update = """
        UPDATE services
        SET time_slots = JSON_SET(time_slots, %s, %s)
        WHERE service_name = %s
    """
    cursor.execute(sql_update, (json_path, remaining - 1, service_name))
    sql_create = """
        INSERT INTO booked_services (user_id, service_name, date, time)
        VALUES (%s, %s, %s, %s)
    """
    cursor.execute(sql_create, (user_id, service_name, date, time))
    conn.commit()
    cursor.close()
    conn.close()

# This function has an atomic or consistency problem. Not serious if the current is small. Need ti be discussed.
@services_blueprint.route('/api/cancel_booking', methods=['POST'])
@jwt_required()
# def cancelBooking():
#     data = request.get_json()
#     booking_id = data['booking_id']
#     service_name = data['service_name']
#     date = data['date']
#     time = data['time']
#     sql_read = """
#         select time_slots from services
#         where service_name = %s
#     """
#     json_path = '$."{}"."{}"'.format(date, time)
#     sql_update_services = """
#         UPDATE services
#         SET time_slots = JSON_SET(time_slots, %s, %s)
#         WHERE service_name = %s
#     """
#     sql_update_booking = """
#         UPDATE booked_services
#         SET status = -1
#         WHERE booking_id = %s
#     """

#     conn = mysql.connector.connect(**config)
#     cursor = conn.cursor()
#     cursor.execute(sql_read, (service_name,))
#     result = cursor.fetchall()
#     remaining = json.loads(result[0][0])[date][time]
#     # Update the database and return modified `timeSlots` directly because they just look the same.
#     cursor.execute(sql_update_services, (json_path, remaining + 1, service_name))
#     conn.commit()
#     new_result = json.loads(result[0][0])
#     # This mutation is inplace
#     new_result[date][time] = remaining + 1
#     # Then update the booking record
#     cursor.execute(sql_update_booking, (booking_id,))
#     conn.commit()
#     cursor.close()
#     conn.close()
#     return jsonify({ "timeSlots": new_result, "bookedService": { 'service_name': '' } })
def cancelBooking():
    data = request.get_json()
    user_id = data['user_id']
    booking_id = data['booking_id']
    service_name = data['service_name']
    date = data['date']
    time = data['time']

    try:
        # 数据库操作
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()

        # 构建 Redis 键
        redis_key = f"booked_service:{user_id}:{service_name}"

        # 获取当前时间槽信息
        cursor.execute("SELECT time_slots FROM services WHERE service_name = %s", (service_name,))
        result = cursor.fetchall()
        time_slots = json.loads(result[0][0])
        remaining = time_slots[date][time]

        # 更新时间槽
        time_slots[date][time] = remaining + 1
        json_path = '$."{}"."{}"'.format(date, time)
        cursor.execute("UPDATE services SET time_slots = JSON_SET(time_slots, %s, %s) WHERE service_name = %s", (json_path, remaining + 1, service_name))

        # 更新 booked_services 表
        cursor.execute("UPDATE booked_services SET status = -1 WHERE booking_id = %s", (booking_id,))
        conn.commit()

        # 更新 Redis 缓存
        # 清除或更新该用户的已预订服务信息
        redis_client.delete(redis_key)

        cursor.close()
        conn.close()

        return jsonify({"timeSlots": time_slots})
    except Exception as e:
        # 如果数据库操作失败，则返回错误信息
        return jsonify({"error": str(e)}), 500