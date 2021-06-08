# -*- coding: utf-8 -*-

from eternity_backend_server.config import SUBSTRATE_URL

from eternity_backend_server.blueprints.ipfs.ipfs import check_code
import json
from substrateinterface import SubstrateInterface, Keypair
from substrateinterface.exceptions import SubstrateRequestException

def upload_ipfshash(account, ipfshash):
    checkcode = check_code(ipfshash)
    if checkcode == False:
        raise ValueError("Failed to send: {}".format("This [ipfshash] is illegal! Please enter the correct [ipfshash]."))
        # return jsonify({"result":"",
        #                 "code":"404"}), 404

    substrate = SubstrateInterface(
        url=SUBSTRATE_URL,
        ss58_format = 42,
        type_registry_preset='default'
    )
    account_name = "//"+account
    keypair = Keypair.create_from_uri(account_name)
    call = substrate.compose_call(
        call_module='DispSigMoudle',
        call_function='transfer',
        call_params={
            'ipfshash':ipfshash
        }
    )
    extrinsic = substrate.create_signed_extrinsic(call=call, keypair=keypair)

    try:
        receipt = substrate.submit_extrinsic(extrinsic, wait_for_finalization=True)
        # print("Extrinsic '{}' sent and included in block '{}'".format(receipt.extrinsic_hash, receipt.block_hash))
        return {
            "extrinsic_hash": receipt.extrinsic_hash,
            "block_hash": receipt.block_hash,
        }

    except SubstrateRequestException as e:
        raise ValueError("Failed to send: {}".format(e))
        # return {
        #     "result": "Failed to send: {}".format(e),
        #     "code": "404"
        # }