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
})

# change needed in pushcontracttrasaction.js
# eos = Eos({
#   keyProvider: wif,
#   httpEndpoint: httpEndpointAddress,
#   chainId: '038f4b0fc8ff18a4f0842a8f0564611f6e96e8535901dd45e43ac8691a1c4dca',  <---Jungle chainId here
# })

def make_transaction():
    response = eos.push_transaction('eosio.token', 'transfer', 'jungletimohe', 'active', {
        "from": "jungletimohe",
        "to": "lioninjungle",
        "quantity": "1.0000 EOS",
        "memo": "testtimo"
    })
    return f"{response['transaction_id']};{response['processed']['block_num']}",

def get_transaction(transaction_id_and_block_num):
    data = {
        "id": transaction_id_and_block_num.strip(";").split(";")[0],
        "block_num_hint": int(transaction_id_and_block_num.strip(";").split(";")[1])
    }
    r = requests.post(
        f'http://193.93.219.219:8888/v1/history/get_transaction', json=data)
    response = json.loads(r.text)
    return response


print(make_transaction())
# print(get_transaction(
    # "da436a0ecee41487addc3642a6625560f5294f4d225407a7a77c66cb6d6816b4;21824439"))

