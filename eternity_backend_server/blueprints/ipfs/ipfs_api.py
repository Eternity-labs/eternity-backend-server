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

from eternity_backend_server.blueprints.ipfs.ipfs import upload_data, get_data_by_ipfsHash, check_code
import os
from threading import Thread

import threading
import time
import random

import json

from eternity_backend_server.extensions import db, csrf_protect
import ipfshttpclient

ipfs_bp = Blueprint("ipfs", __name__, static_folder="../static")

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@ipfs_bp.route("/upload", methods=["POST"])
def upload():
    data = request.get_json()
    res = upload_data(data)
    return jsonify({"ipfshash": res})

@csrf_protect.exempt
@ipfs_bp.route("/getdatabyipfshash/<string:ipfshash>", methods=["GET", "POST"])
def getdatabyipfshash(ipfshash):
    data_dict = get_data_by_ipfsHash(ipfshash)
    return jsonify({"data":data_dict, "ipfshash":ipfshash}), 200


@csrf_protect.exempt
@ipfs_bp.route("/checkcode/<string:ipfshash>", methods=["GET", "POST"])
def checkcode(ipfshash):
    return jsonify({"legal": check_code(ipfshash)}), 200