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
    current_app,
    g
)
import requests

from eternity_backend_server.extensions import csrf_protect
from eternity_backend_server.blueprints.datamin.datamin import bishijieclient
from eternity_backend_server.extensions import db
from eternity_backend_server.blueprints.datamin.models import DATAMINFLAG, DATAMIN
from eternity_backend_server.blueprints.datamin.etherscanclient import etherscanclient
from eternity_backend_server.extensions import db
from eternity_backend_server.settings import ETHERSCAN_APIKEY, ETHERSCAN_TOKEN

datamin_bp = Blueprint("datamin", __name__, static_folder="../static")

@csrf_protect.exempt
@datamin_bp.route("/news/get", methods=["GET"])
def get_view():
    """获取news数据库里的内容

       @@@
       ### args
       None

       ### return
       ```json
       {"code": xxxx, "msg": "xxx", "data": null}
       ```
       @@@
       """

    datamin = DATAMIN.query.filter().first()
    return jsonify(datamin.datalist)




@csrf_protect.exempt
@datamin_bp.route("/news/send_heartbeat", methods=["GET"])
def send_heartbeat():
    dataminflag = DATAMINFLAG.query.filter(DATAMINFLAG.id==1).first()
    if dataminflag.flag == 1:
        datamin = DATAMIN.query.filter(DATAMIN.id==1).first()
        return jsonify({
            "result": "is update",
            "message": datamin.datalist,
            "flag": dataminflag.flag
        })
    dataminflag.flag = 1
    result = bishijieclient()
    datamin = DATAMIN.query.filter(DATAMIN.id==1).first()
    datamin.type = result.get("info")
    datamin.datalist = result.get("info_list")
    db.session.commit()
    return jsonify({
        "result": "success update",
        "message": datamin.datalist,
        "flag": dataminflag.flag
    })

@csrf_protect.exempt
@datamin_bp.route("/eth/contractaddress", methods=["GET"])
def contractaddress():
    ethclient = etherscanclient(ETHERSCAN_TOKEN, ETHERSCAN_APIKEY)
    result = ethclient.contractaddress()
    return jsonify(result)


@csrf_protect.exempt
@datamin_bp.route("/eth/tokencontractaddress", methods=["GET"])
def tokencontractaddress():
    ethclient = etherscanclient(ETHERSCAN_TOKEN, ETHERSCAN_APIKEY)
    result = ethclient.tokencontractaddress()
    return jsonify(result)


@csrf_protect.exempt
@datamin_bp.route("/eth/token_info", methods=["GET"])
def token_info():
    ethclient = etherscanclient(ETHERSCAN_TOKEN, ETHERSCAN_APIKEY)
    result = ethclient.token_info()
    return jsonify(result)


@csrf_protect.exempt
@datamin_bp.route("/eth/token_transfers", methods=["GET"])
def token_transfers():
    ethclient = etherscanclient(ETHERSCAN_TOKEN, ETHERSCAN_APIKEY)
    result = ethclient.token_transfers()
    return jsonify(result)

