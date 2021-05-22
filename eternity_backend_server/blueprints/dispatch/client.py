from flask import Flask

import hashlib
import ipfshttpclient
import time
# from eternity_backend_server.utils import Hash
from eternity_backend_server.others.snowid.snowid import IdWorker

import requests
import logging
import socket

class ValidationError(Exception):
    pass


class BadSignature(Exception):
    pass

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

def is_open(ip,port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    try:
        s.connect((ip,int(port)))
        s.shutdown(2)
        return 1
    except:
        return -1

LOG = logging.getLogger(__name__)


app = Flask(__name__)




class DispatchObjectClient():
    def __init__(self, HOST, PORT):
        time.sleep(1)
        self.snowidworker = None

        # 节点信息
        self.id = None
        self.timestamp = None

        # 权限控制
        self.active = False

        # 节点监察
        self.host = HOST
        self.port = PORT
        if "://" in HOST:
            if HOST[-1] == "/":
                HOST = HOST[:-1]
            entity = HOST.split("/")[2].split(":")
            HOST = entity[0]
            self.host = HOST
            PORT = int(entity[1])
            self.port = PORT
        if not isinstance(PORT, int):
            raise TypeError("PORT must be an instance of int")
        self.BASEURL = "https://{HOST}:{PORT}".format(HOST=HOST, PORT=PORT)
        connect_cnt = is_open(self.host, self.port) + is_open(self.host, self.port) + is_open(self.host, self.port)
        if connect_cnt == 3:
            print("链接成功")
        else:
            raise ValidationError("链接失败!!!")


    def get(self, url, params=""):

        response = requests.get("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), params=params)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()

    def post(self, url, data):

        response = requests.post("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), json=data)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()


@app.route("/")
@app.route("/list")
def index():
    pass



@app.route("/add", methods=["GET", "POST"])
def adddispatch():
    pass

if __name__ == '__main__':
    print(get_host_ip())
    a = DispatchObjectClient("47.98.100.48", 150070)