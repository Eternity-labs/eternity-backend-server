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
from eternity_backend_server.extensions import csrf_protect
from eternity_backend_server.blueprints.analiysis.analiysis import get_ipfs_model_file

analiysis_bp = Blueprint("analiysis", __name__, static_folder="../static")

@csrf_protect.exempt
@analiysis_bp.route("/substrate/listnodeinfo", methods=["GET"])
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


@csrf_protect.exempt
@analiysis_bp.route("/substrate/getanaliysisfile", methods=["POST"])
def get_analiysis_file():
    data = request.get_json()
    key1 = data["key1"]
    key2 = data["key2"]
    ipfshash = data["ipfshash"]
    result_file = get_ipfs_model_file(key1, key2, ipfshash)
    return jsonify(result_file)


@csrf_protect.exempt
@analiysis_bp.route("/feargreedindex", methods=["GET"])
def fear_greed_index():
    data = {
        "index": 0.78
    }
    return jsonify(data)

@csrf_protect.exempt
@analiysis_bp.route("/officalpoolportfolio", methods=["GET"])
def offical_pool_portfolio():

    data = [
        {
            "name": "BTC",
            "Volume": 1300,
            "Rate": 0.1,
            "Price": 188
        },{
            "name": "ETH",
            "Volume": 1300,
            "Rate": 0.1,
            "Price": 188
        },{
            "name": "DOT",
            "Volume": 1300,
            "Rate": 0.1,
            "Price": 188
        },{
            "name": "ENL",
            "Volume": 1300,
            "Rate": 0.1,
            "Price": 188
        },
    ]
    return jsonify(data)



@csrf_protect.exempt
@analiysis_bp.route("/spotpricedifference", methods=['GET'])
def spot_price_difference():
    # 返回 DOT 火币,币安,okex,抹茶,uniswap,heco交易所现货价格的最大价差
    data = [
        {
            "dex": "huobi",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "binance",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "okex",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "mxc",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "uniswap",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "heco",
            "price": 100,
            "gasfee": 1,
        },
    ]
    return jsonify(data)


@csrf_protect.exempt
@analiysis_bp.route("/contractpricedifference", methods=["GET"])
def contract_price_difference():
    # 返回 DOT 火币,币安,okex,抹茶,合约价格的最大价差
    data = [
        {
            "dex": "huobi",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "binance",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "okex",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "mxc",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "uniswap",
            "price": 100,
            "gasfee": 1,
        },
        {
            "dex": "heco",
            "price": 100,
            "gasfee": 1,
        },
    ]
    return jsonify(data)