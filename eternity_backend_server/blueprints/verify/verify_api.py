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
from eternity_backend_server.blueprints.dispatch.dispatch import upload_ipfshash

verify_bp = Blueprint("verify", __name__, static_folder="../static")



@csrf_protect.exempt
@verify_bp.route("/substrate/listnodeinfo", methods=["GET"])
def list_node_info():
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