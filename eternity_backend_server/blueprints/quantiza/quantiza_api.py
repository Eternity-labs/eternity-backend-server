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

quantize_bp = Blueprint("quantize", __name__, static_folder="../static")

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@quantize_bp.route("/modellist", methods=["GET"])
def modellist():
    data = [
        {
            "Name": "A",
            "Ipfshash": "0x1234131",
            "AccountId": "gegwegwetg23234"
        },
        {
            "Name": "B",
            "Ipfshash": "0x1234131",
            "AccountId": "qwgqgwqgwert34t23"
        },
        {
            "Name": "C",
            "Ipfshash": "0x1234131",
            "AccountId": "ereryert3414121"
        },
        {
            "Name": "D",
            "Ipfshash": "0x1234131",
            "AccountId": "qwgqwgqwe12312qgddbh"
        },
        {
            "Name": "E",
            "Ipfshash": "0x1234131",
            "AccountId": "1231qwfqwgqg14"
        },
        {
            "Name": "F",
            "Ipfshash": "0x1234131",
            "AccountId": "wegqwgqwgwweqwe"
        },
    ]
    return jsonify(data)