# -*- coding: utf-8 -*-
from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for,
    abort,
    jsonify,
    g
)
from flask_login import login_required, login_user, logout_user, current_user
from eternity_backend_server.utils import flash_errors, redirect_back, create_address_by_privkey
# from eternity_backend_server.extensions import csrf_protect, dispatchList
from eternity_backend_server.config import REDIS_IP, REDIS_PORT, REDIS_DB, REDIS_NAME, REDIS_PASSWORD

from eternity_backend_server.extensions import db, csrf_protect, dispatchList
from eternity_backend_server.Dispatch import Dispatch

import os
from threading import Thread

import threading
import time
import random

import redis
import json

dispatch_bp = Blueprint("dispatch", __name__, static_folder="../static")

class ValidationError(Exception):
    pass



def vote_thread():
    redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
    client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)

    while 1:
        data_bytes = client.lpop(REDIS_NAME)
        if data_bytes == None:
            raise ValidationError("当前队列里没有调度节点！")

        data = str(data_bytes,'utf-8')
        params_dict = json.loads(data)
        params_dict["active"] = True
        print(params_dict)
        time.sleep(10)
        client.rpush(REDIS_NAME, json.dumps(params_dict))


@csrf_protect.exempt
@dispatch_bp.route("/")
@dispatch_bp.route("/list")
def index():
    redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
    client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)
    result = client.lrange(REDIS_NAME, 0, -1)
    result_json = []
    for item_bytes in result:
        item_str = str(item_bytes,'utf-8')
        item_dict = json.loads(item_str)
        result_json.append(item_dict)
    return jsonify({
        "dispatchList":  result_json
    })

@csrf_protect.exempt
@dispatch_bp.route("/add", methods=["GET", "POST"])
def adddispatch():
    data = request.get_json()
    ip = data["ip"]
    port = data["port"]
    privkey = data["privkey"]
    nodeMsg = create_address_by_privkey(privkey)
    publickey = nodeMsg["publicKeyHex"]
    address = nodeMsg["address"]
    addJson = {
        "privkey": privkey,
        "publickey": publickey,
        "address": address,
        "version": "0.1",
        "ip": ip,
        "port": port,
        "substrate": {
            "nodeport": "none",
            "nodeip": "none"
        }
    }

    redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
    client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)
    all_result = client.lrange(REDIS_NAME, 0, -1)

    for item_bytes in all_result:
        item_str = str(item_bytes,'utf-8')
        item_dict = json.loads(item_str)
        if addJson["privkey"] == item_dict["privkey"]:
            return jsonify({"result": "已经添加过该调度节点了"})


    dispatchobject = Dispatch(ip, port, addJson["version"], privkey, publickey, address, addJson["substrate"])
    dispatchNode = {}
    dispatchNode["id"] = dispatchobject.id
    dispatchNode["ip"] = dispatchobject.ip
    dispatchNode["port"] = dispatchobject.port
    dispatchNode["version"] = dispatchobject.version
    dispatchNode["privkey"] = dispatchobject.privkey
    dispatchNode["publickey"] = dispatchobject.publickey
    dispatchNode["address"] = dispatchobject.address
    dispatchNode["active"] = dispatchobject.active
    dispatchNode["substrate"] = dispatchobject.substrateMsg
    # print(dispatchNode)
    client.rpush(REDIS_NAME, json.dumps(dispatchNode))
    return jsonify({
        "result": "successful",
        "DetailMsg": dispatchNode
    })

@csrf_protect.exempt
@dispatch_bp.route("/getvotenode", methods=["GET", "POST"])
def getvotenode():
    redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
    client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)
    all_result = client.lrange(REDIS_NAME, 0, -1)
    is_have_vote = 0
    for item_bytes in all_result:
        item_str = str(item_bytes,'utf-8')
        item_dict = json.loads(item_str)
        if item_dict["active"] == True:
            voter = item_dict
            is_have_vote = 1

    if is_have_vote == 1:
        return jsonify({"voter": voter})
    else:
        return jsonify({"result": "当前所有调度节点均无调度权限。"})

@csrf_protect.exempt
@dispatch_bp.route("/votenode", methods=["GET", "POST"])
def votenode():
    redisPool = redis.ConnectionPool(host=REDIS_IP, port=REDIS_PORT, db=REDIS_DB)
    client = redis.Redis(connection_pool=redisPool, password=REDIS_PASSWORD)

    result = client.lrange(REDIS_NAME, 0, -1)
    have_voter = 0  # 判断第一次执行这个命令的时候 是否存在
    result_json = []  # 存储序列化的调度节点的信息
    items_len = len(result)  # 调度节点的数量
    vote_index = -1  # 有权限的调度节点的下标

    for item_bytes in result:
        item_str = str(item_bytes, 'utf-8')
        item_dict = json.loads(item_str)
        if item_dict["active"] == True:
            have_voter += 1
        result_json.append(item_dict)

    if have_voter == 0:
        p1 = threading.Thread(target=vote_thread, args=())
        p1.start()
        return jsonify({"result": "开始选举线程"})
    else:
        return jsonify({"result": "已经开启过选举线程"})
