# -*- coding: utf-8 -*-

import time
import random

import json

import ipfshttpclient

def upload_data(data):
    ip = data.get("ip")
    address = data.get("address")
    detail = data.get("detail")
    timestamp = time.time()
    need_upload_msg = {
        "timestamp": timestamp,
        "ip": ip,
        "detail": detail,
        "address": address,
        "checkcode": True
    }
    upload_msg_str = json.dumps(need_upload_msg)
    client = ipfshttpclient.connect()

    res = client.add_str(upload_msg_str)
    return res

def get_data_by_ipfsHash(ipfshash):
    client = ipfshttpclient.connect()
    data_bytes = client.cat(ipfshash)
    data_str = str(data_bytes, encoding = "utf-8")
    data_dict = json.loads(data_str)
    return data_dict

def check_code(ipfshash):
    data = get_data_by_ipfsHash(ipfshash)
    if data is None:
        raise ValueError("IPFS data is Null, Please enter the correct ipfshash.")
    checkcode = data.get("checkcode")
    if checkcode==True:
        return checkcode
    else:
        return False