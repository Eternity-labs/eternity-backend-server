# -*- coding: utf-8 -*-
"""User views."""
from flask import Blueprint, render_template, jsonify
from flask_login import login_required
from eternity_backend_server.extensions import csrf_protect

user_bp = Blueprint("user", __name__, url_prefix="/users", static_folder="../static")


@user_bp.route("/")
@login_required
def members():
    """List members."""
    return render_template("users/members.html")

@csrf_protect.exempt
@user_bp.route("/accountinfo/<string:address>", methods=["GET"])
def account_info(address):
    data = {
            "AccountId": address,
            "Token": "108591",
            "Income": "9999",
            "Quan": [
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },
                {
                    "model": "A",
                    "Value": "100",
                    "quanNode": "0x123411"
                },

    ]
    }

    return jsonify(data)