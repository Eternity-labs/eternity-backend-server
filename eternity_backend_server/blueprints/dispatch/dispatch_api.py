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
from eternity_backend_server.blueprints.ipfs.ipfs import check_code
from eternity_backend_server.blueprints.dispatch.dispatch import upload_ipfshash
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

dispatch_bp = Blueprint("dispatch", __name__, static_folder="../static")

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@dispatch_bp.route("/substrate/<string:account>/upload/ipfshash/<string:ipfshash>", methods=["POST"])
def upload_ipfshash_view(account, ipfshash):
    data = upload_ipfshash(account, ipfshash)
    extrinsic_hash = data.get("extrinsic_hash")
    block_hash = data.get("block_hash")
    block_number = data.get("block_number")

    return jsonify({
            "result": "Extrinsic '{}' sent and included in block '{}'".format(extrinsic_hash, block_hash),
            "extrinsic_hash": extrinsic_hash,
            "block_hash": block_hash,
            "block_number": block_number,
            "code": "201"
        }), 201

@csrf_protect.exempt
@dispatch_bp.route("/substrate/<string:account>/get/<string:blockhash>", methods=["GET", "POST"])
def get_ipfshash_by_blockhash_view(blockhash):
    substrate = SubstrateInterface(
        url="wss://service.eternitylab.cn",
        ss58_format=42,
        type_registry_preset='default'
        # wss://service.eternitylab.cn
    )
    substrate.get_block_number(blockhash)


@csrf_protect.exempt
@dispatch_bp.route("/substrate/listnodeinfo", methods=["GET"])
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
            "name":"Axxx",
            "IP": "127.0.0.1:9000",
            "Status": "online",
            "AccountId": "0x123156184",
        },
    ]
    return jsonify(data)