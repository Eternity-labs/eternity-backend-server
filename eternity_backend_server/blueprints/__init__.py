# import redis
# import json
# import random
# import time
#
# from eternity_backend_server.config import REDIS_IP, REDIS_PORT, REDIS_DB, REDIS_NAME, REDIS_PASSWORD
# redisPool = redis.ConnectionPool(host='192.168.80.141', port=6379, db=5)
# client = redis.Redis(connection_pool=redisPool)
#
#
# class ValidationError(Exception):
#     pass
#
#
#
# def vote_thread():
#     redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
#     client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)
#
#     # result = client.lrange(REDIS_NAME, 0, -1)
#     # have_voter = 0      # 判断第一次执行这个命令的时候 是否存在
#     # result_json = []  # 存储序列化的调度节点的信息
#     # items_len = len(result) # 调度节点的数量
#     # vote_index = -1  # 有权限的调度节点的下标
#     #
#     # for item_bytes in result:
#     #     item_str = str(item_bytes,'utf-8')
#     #     item_dict = json.loads(item_str)
#     #     if item_dict["active"] == True:
#     #         have_voter+=1
#     #     result_json.append(item_dict)
#     #
#     #
#     # if have_voter == 0:
#     #     first_index = random.randint(0, items_len-1)
#
#     while 1:
#         data_bytes = client.lpop(REDIS_NAME)
#         if data_bytes == None:
#             raise ValidationError("当前队列里没有调度节点！")
#
#         data = str(data_bytes,'utf-8')
#         params_dict = json.loads(data)
#         params_dict["active"] = True
#         print(params_dict)
#         time.sleep(10)
#         client.rpush(REDIS_NAME, json.dumps(params_dict))
#
#     # return jsonify({"Voter": params_dict})
#
#
# #
# # # client.delete("test")
# # # 顺序插入五条数据到redis队列，sort参数是用来验证弹出的顺序
# # num = 0
# # while num < 3:
# #
# #     num = num + 1
# #     # params info
# #     params_dict = {"name": f"test {num}", "sort":num}
# #
# #     client.rpush("test", json.dumps(params_dict))
# #
# #     # 查看目标队列数据
# #     result = client.lrange("test", 0, -1)
# #     print(result)
# #     import time
# #     time.sleep(1)
# #
# # while 1:
# #     data_bytes = client.lpop("test")
# #     data = str(data_bytes,'utf-8')
# #     print(data)
# #     result = client.lrange("test", 0, -1)
# #     print(result)
# #     params_dict = json.loads(data)
# #     client.rpush("test", json.dumps(params_dict))
# #     import time
# #     time.sleep(1)
# if __name__ == '__main__':
#     vote_thread()