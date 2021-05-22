# -*- coding: utf-8 -*-
"""Helper utilities and decorators."""
try:
    from urlparse import urlparse, urljoin
except ImportError:
    from urllib.parse import urlparse, urljoin

from flask import request, redirect, url_for, current_app

from flask import flash
import hashlib
import base64
import sha3
from ecdsa import SigningKey, SECP256k1
import os
from eth_account import Account

def flash_errors(form, category="warning"):
    """Flash all errors for a form."""
    for field, errors in form.errors.items():
        for error in errors:
            flash(f"{getattr(form, field).label.text} - {error}", category)

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def redirect_back(default='public.home', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return redirect(target)
    return redirect(url_for(default, **kwargs))


def ecdsa_sign(self, encode_transaction, privkey, hashfunc=hashlib.sha256):
    signning_key = SigningKey.from_string(bytes.fromhex(privkey), curve=SECP256k1)
    # encode_transaction = respBody['respBody']['encodedTransaction']
    # base64解密
    transaction = self.base64_decode(encode_transaction)
    # 获取hash
    hashedMsg = self.Hash(transaction)
    bytes_hashed = bytes(bytearray.fromhex(hashedMsg))
    # 签名
    signature = signning_key.sign(bytes_hashed, hashfunc=hashfunc)
    # base64加密
    transaction_encode = self.base64_encode(signature)
    return transaction_encode

def base64_decode(self, base_data):
    """
    base64解密
    :param base_data:
    :return:
    """
    bytes_data = base64.b64decode(base_data)
    return bytes_data

def base64_encode(self, bytes_data):
    """
    base64加密
    :param bytes_data:
    :return:
    """
    base_data = base64.b64encode(bytes_data)
    return bytes.decode(base_data)

def Hash(self, msg):
    """
    hash加密
    :return:
    """
    k = sha3.keccak_256()
    k.update(msg)
    return k.hexdigest()




def generate_addr(priv=None):
    if priv == None:
        account = Account.create()
    else:
        try:
            account = Account.privateKeyToAccount(priv)
        except Exception as e:
            return {"result": "error", "error":e}
    return {"result": "success",
            "payload":
                {"addr": account.address,
                 "priv": account.privateKey.hex(),
                 "pubv": str(account._key_obj.public_key).lower()
                 }}



def create_privkey():
    return os.urandom(32)


def create_address_by_privkey(privkey):
    if privkey[:2] == "0x":
        account = generate_addr(priv=privkey[2:])
    else:
        account = generate_addr(priv=hex(int(privkey))[2:])

    addr = account["payload"]["addr"]
    data = {
        "privateKeyHex": account["payload"]["priv"],
        "publicKeyHex": account["payload"]["pubv"],
        "privateKeyInt": str(int(account["payload"]["priv"], 16)),
        "publicKeyInt": str(int(account["payload"]["pubv"], 16)),
        "address": addr,
    }
    return data

# if __name__ == '__main__':
#     priv_key = "18e14a7b6a307f426a94f8114701e7c8e774e7f9a47e2c2035db29a206321725"
#     signning_key = SigningKey.from_string(bytes.fromhex(priv_key), curve=SECP256k1)
#     # signning_key = SigningKey.generate(curve=SECP256k1)
#     privkey = signning_key.to_string()
#     print(privkey)
#     verifing_key = signning_key.get_verifying_key()
#     print(verifing_key)
#     data = "hello, world"
#     print(data)
#     bytes_hashed = str.encode(data)
#     print(bytes_hashed)
#     # 签名
#     signature = signning_key.sign(bytes_hashed, hashfunc=hashlib.sha256)
#     print(signature)
#     print(type(signature))
#     print(signature.hex())
#
#     result = verifing_key.verify(signature=signature, data=bytes_hashed, hashfunc=hashlib.sha256)
#     print(result)
