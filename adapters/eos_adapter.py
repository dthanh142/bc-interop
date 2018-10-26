import requests
import json

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
                "memo": "created by noprom"
            }
    }
	r = requests.post(
		f'{JUNGLE_URL}/v1/chain/abi_json_to_bin', json=data)
	response = json.loads(r.text)
	return response["binargs"]
	
print(get_tx_bin())

def sign_transaction():
	data = [{
		"expiration": "2018-10-26T15:30:32.000",
		"ref_block_num": 21149807,
		"ref_block_prefix": 3590041248,
		"context_free_actions": [],
		"actions": [{
			"account": "eosio.token",
			"name": "transfer",
			"authorization": [{
					"actor": "testertimohe",
					"permission": "active"
			}],
			"data": "0000000000ea305500000000487a2b9d102700000000000004454f53000000001163726561746564206279206e6f70726f6d"
		}],
		"signatures": []
	},
		["EOS6gXwNz2SKUNAZcyjzVvg6KdNgA1bSuVzCr8c5yWkGij52JKx8V"], ""
	]
	r = requests.post(
		f'http://localhost:8888/v1/wallet/sign_transaction', json=data)
	response = json.loads(r.text)
	return response



