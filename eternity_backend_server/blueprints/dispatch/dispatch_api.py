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

dispatch_bp = Blueprint("dispatch", __name__, static_folder="../static")

class ValidationError(Exception):
    pass

@csrf_protect.exempt
@dispatch_bp.route("/substrate/<string:account>/upload/ipfshash/<string:ipfshash>", methods=["POST"])
def uploadipfshash(account, ipfshash):
    data = upload_ipfshash(account, ipfshash)
    extrinsic_hash = data.get("extrinsic_hash")
    block_hash = data.get("block_hash")
    return jsonify({
            "result": "Extrinsic '{}' sent and included in block '{}'".format(extrinsic_hash, block_hash),
            "extrinsic_hash": extrinsic_hash,
            "block_hash": block_hash,
            "code": "201"
        }), 201