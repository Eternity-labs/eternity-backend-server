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

from eternity_backend_server.extensions import db, csrf_protect
import ipfshttpclient

from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

import os
import json
from scalecodec.type_registry import load_type_registry_file
from pprint import pprint

from eternity_backend_server.config import TYPE_REGISTRY_JSON
from eternity_backend_server.blueprints.quantiza.quantiza import model_list, search_node


quantize_bp = Blueprint("quantize", __name__, static_folder="../static")

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@quantize_bp.route("/modellist", methods=["GET"])
def model_list_view():
    result = model_list()
    return jsonify(result)


@csrf_protect.exempt
@quantize_bp.route("/searchnode/<string:id_or_hash>", methods=["GET"])
def search_node_view(id_or_hash):

    result = search_node(id_or_hash)
    return jsonify(result)



@csrf_protect.exempt
@quantize_bp.route("/substrate/listnodeinfo", methods=["GET"])
def list_node_info_view():
    data = [
        {
            "name":"Axxx",
            "IP": "127.0.0.1:9000",
            "Status": "online",
            "AccountId": "0x123156184",
        },
        {
            "name":"Bxxx",
            "IP": "127.0.0.1:9000",
            "Status": "offline",
            "AccountId": "0x123156184",
        },
        {
            "name":"Cxxx",
            "IP":"127.0.0.1:9000",
            "Status": "online",
            "AccountId":"0x123156184",

        },
        {
            "name":"Axxx",
            "IP": "127.0.0.1:9000",
            "Status": "online",
            "AccountId": "0x123156184",
        },
        {
            "name": "Axxx",
            "IP": "127.0.0.1:9000",
            "Status": "online",
            "AccountId": "0x123156184",
        },
    ]
    return jsonify(data)

@csrf_protect.exempt
@quantize_bp.route("/worthtoken", methods=["GET"])
def worth_token_view():
    data = [
        {
            "Name": "btc"
        },
        {
            "Name": "eth"
        },
        {
            "Name": "dot"
        },
        {
            "Name": "enl"
        },
    ]
    return jsonify(data)