import requests
import json


# data = {
# 	"id": "curltext",
# 	"method": "payto",
#     "params": {"destination": "mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", "amount": "0.00345678"}
# }
# r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
# response = json.loads(r.text)
# print (response)

def send_transaction():

    data = {
        "id": "curltext",
        "method": "payto",
        "params": {"destination": "mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", "amount": "0.00345678", "memo": "alsdkjfklasjflkj"}
    }
    r = requests.post(
        'http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
    response = json.loads(r.text)
    unsigned_tx = response["result"]["hex"]

    data = {
        "id": "curltext",
        "method": "broadcast",
        "params": {"tx": unsigned_tx}
    }
    r = requests.post(
        'http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
    response = json.loads(r.text)
    print(response)


def get_transaction():
	data = {
		"id": "curltext",
		"method": "gettransaction",
		"params": {"txid": "49ca013a5843fea814816665a4ffecc62b8cfd9be49146d104a25418608725f4"}
	}
	r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
	response = json.loads(r.text)
	print(response)


send_transaction()