import hashlib
import ipfshttpclient
import time
# from eternity_backend_server.utils import Hash
from eternity_backend_server.others.snowid.snowid import IdWorker

class Dispatch():
    def __init__(self, IP, PORT, version, privkey, publickey, address, substrateMsg):

        time.sleep(1)
        self.snowidworker = IdWorker(1, 2, 0)

        # 节点信息
        self.id = self.snowidworker.get_id()
        self.timestamp = time.time()

        # 权限控制
        self.active = False

        # 节点设置
        self.ip = IP
        self.port = PORT
        self.version = version
        self.privkey = privkey
        self.publickey = publickey
        self.address = address
        self.substrateMsg = substrateMsg

    def Print(self):
        print(self.id, self.timestamp)