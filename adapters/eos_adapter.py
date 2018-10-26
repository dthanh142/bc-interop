import requests
import json
import pprint

JUNGLE_URL = "http://jungle.cryptolions.io:18888"
LOCAL_EOS_URL = "http://localhost:8888"


def get_tx_bin():
	data = {
		"code": "eosio.token",
		"action": "transfer",
		"args": {
				"from": "eosio",
				"to": "noprom",
				"quantity": "1.0000 EOS",
				"memo": "test successful"
		}
	}
	r = requests.post(
		f'{JUNGLE_URL}/v1/chain/abi_json_to_bin', json=data)
	response = json.loads(r.text)
	return response["binargs"]


def get_head_block_num():
	r = requests.get(f'{JUNGLE_URL}/v1/chain/get_info')
	response = json.loads(r.text)
	return response["head_block_num"]


def get_block_num_and_expiration(block_nr):
	data = {"block_num_or_id": block_nr}
	r = requests.post(f'{JUNGLE_URL}/v1/chain/get_block', json=data)
	response = json.loads(r.text)
	return response["ref_block_prefix"], response["timestamp"]


def get_tx_dict():
	tx = {}
	tx["data"] = get_tx_bin()
	tx["ref_block_num"] = get_head_block_num()
	tx["ref_block_prefix"], tx["expiration"] = get_block_num_and_expiration(
		tx["ref_block_num"])
	# increase timestamp by two minutes
	tx["expiration"] = tx["expiration"][:14] + \
		str(int(tx["expiration"][14:16])+2) + tx["expiration"][16:]
	return tx


def sign_transaction():
	tx_data = get_tx_dict()
	data = [{
			"expiration": tx_data["expiration"],
			"ref_block_num": tx_data["ref_block_num"],
			"ref_block_prefix": tx_data["ref_block_prefix"],
			"context_free_actions": [],
			"actions": [{
				"account": "eosio.token",
				"name": "transfer",
				"authorization": [{
						"actor": "testertimohe",
					"permission": "active"
				}],
				"data": tx_data["data"]
			}],
			"signatures": []
			},
			["EOS6gXwNz2SKUNAZcyjzVvg6KdNgA1bSuVzCr8c5yWkGij52JKx8V"], ""
			]
	r = requests.post(
		f'http://localhost:8888/v1/wallet/sign_transaction', json=data)
	response = json.loads(r.text)
	return response
