from eosjs_python import Eos
import requests
import json

# 'private': '5KazRYnXDCNougrvuVtZFDMAiB3kr7M2tjGYNJtQQ2Wn3JFRdTM',
# 'public': 'EOS8Vfg6ssQxj66wX9LrFq3EZY8z4EEkiyiQiDc7bwyn65K4YFVwW'}
# jungletimohe

eos = Eos({
    'http_address': 'http://dev.cryptolions.io:38888',
    'key_provider': '5KazRYnXDCNougrvuVtZFDMAiB3kr7M2tjGYNJtQQ2Wn3JFRdTM',
    # get this using 'http://dev.cryptolions.io:38888/v1/chain/get_info'
    # 'chainId': '038f4b0fc8ff18a4f0842a8f0564611f6e96e8535901dd45e43ac8691a1c4dca',
    'expireInSeconds': 60,
    'broadcast': True,
    'debug': True,
    'sign': True,
    'verbose': True,
})

# change needed in pushcontracttrasaction.js
# eos = Eos({
#   keyProvider: wif,
#   httpEndpoint: httpEndpointAddress,
#   chainId: '038f4b0fc8ff18a4f0842a8f0564611f6e96e8535901dd45e43ac8691a1c4dca',  <---Jungle chainId here
# })

def make_transaction():
    return eos.push_transaction('eosio.token', 'transfer', 'jungletimohe', 'active', {
        "from": "jungletimohe",
        "to": "lioninjungle",
        "quantity": "1.0000 EOS",
        "memo": "testtimo"
    })

def get_transaction(transaction_id):
    data = {
        "id": "26cef29a0f19b58084be865e400ce6dbd779296a393a91dff323b17f73700b33"
    }

    r = requests.post(
        f'http://jungle.eosmeso.io:8888/v1/history/get_transaction', json=data)
    response = json.loads(r.text)
    return response


print(make_transaction())
# print(get_transaction("tx_id"))
# print(get_transaction("f7278edea06b657455fc41dafb5df044558cece31816996a47af9416dc11e648"))

