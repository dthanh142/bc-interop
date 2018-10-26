import requests
import json
import pprint

JUNGLE_URL = "http://jungle.cryptolions.io:18888"
LOCAL_EOS_URL = "http://localhost:8888"

# "https://github.com/r12543/pyeos"
# "https://eosio.stackexchange.com/questions/2942/how-to-sign-a-transaction-locally-using-python/2965#2965"
# https://eosio.stackexchange.com/questions/2065/where-is-wallet-rpc-api-documentation
def create_wallet():
	headers = {
		'Cache-Control': 'no-cache',
		'Content-Type': 'application/json',
	}
	# headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}

	data = 'mywallet'

	response = requests.post(
		'http://localhost:9876/v1/wallet/create', headers=headers, data=data)

def create_keys():
	data = ["default", "K1"]
	headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response = requests.post(url="http://127.0.0.1:9876/v1/wallet/create_key", data = data)
	print(response.text)

def listKeys():
	import requests
	url = "http://localhost:9876/v1/wallet/list_keys"
	headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response = requests.request("POST", url, headers=headers)
	print(response.text)

def listWallet():
	url = "http://127.0.0.1:9876/v1/wallet/list_wallets"
	headers = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
	response = requests.request("POST", url, headers=headers)
	print(response.text)

listWallet()

# nodeosd_1 | warn  ...  accepted network connection
# nodeosd_1 | error ... incoming message length unexpected(1414745936), from 172.19.0.1: 39826

listKeys()

transaction = {
    "code": "eosio.token",
    "action": "transfer",
    "args": {
        "from": "eosio",
        "to": "noprom",
        "quantity": "1.0000 EOS",
        "memo": "test successful"
    }
}


def get_tx_bin():
    data = transaction
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


def createWallet():
    """
    Creates a new wallet with the given name.
        :param wallet_name(string): name of the wallet to create
    """
    url = self.base_url + WALLET_API_ENUM.get('CREATE_WALLET')
    return make_post_request(url, json.dumps(wallet_name))


# def get_required_keys():
#     tx_data = get_tx_dict()
#     data = {
#         "available_keys": [
#             "EOS5ySgzeHp9G7TqNDGpyzaCtahAeRcTvPRPJbFey5CmySL3vKYgE",
#             "EOS6MRyAjQq8ud7hVNYcfnVPJqcVpscN5So8BhtHuGYqET5GDW5CV",
#             "EOS6gXwNz2SKUNAZcyjzVvg6KdNgA1bSuVzCr8c5yWkGij52JKx8V"
#         ],
#         "transaction": {
#             "ref_block_num": "100",
#             "ref_block_prefix": "137469861",
#             "expiration": "2017-09-25T06:28:49",
#             "scope": ["initb", "initc"],
#             "actions": [{
#                 "code": "currency",
#                 "type": "transfer",
#                 "recipients": ["initb", "initc"],
#                 "authorization": [{
#                     "account": "initb",
#                     "permission": "active"
#                 }],
#                 "data": "000000000041934b000000008041934be803000000000000"
#             }],
#             "signatures": [],
#             "authorizations": []
#         }
#     }
#     r = requests.post(f'{JUNGLE_URL}/v1/chain/get_required_keys', json=data)
#     response = json.loads(r.text)
#     print(response)


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
