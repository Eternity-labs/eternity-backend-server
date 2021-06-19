import ipfshttpclient
from eternity_backend_server.blueprints.ipfs.aes import PrpCrypt

def get_ipfs_model_file(key1, key2, ipfshash):
    client = ipfshttpclient.connect()
    bytes_encrypt_content = client.cat(ipfshash)
    encrypt_content = str(bytes_encrypt_content, "utf-8")
    filename, aes_content = encrypt_content.split("_")
    pc = PrpCrypt(key1, key2)
    content = pc.decrypt(aes_content)
    result = {filename:content}
    return result