import requests, json


# data = {
# 	"id": "curltext",
# 	"method": "payto",
#     "params": {"destination": "mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", "amount": "0.00345678"}
# }
# r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
# response = json.loads(r.text)
# print (response)

	

data = {
    "id": "curltext",
   	"method": "payto",
    "params": {"destination": "mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", "amount": "0.00345678"}
}
r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
response = json.loads(r.text)
# print(response)
unsigned_tx = response["result"]["hex"]
# print(unsigned_tx)

# data = {
#     "id": "curltext",
#    	"method": "signtransaction",
#     "params": {"tx": unsigned_tx}
# }
# r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
# signed_tx = json.loads(r.text)
# print(signed_tx)

data = {
    "id": "curltext",
   	"method": "broadcast",
    "params": {"tx": unsigned_tx}
}
r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
response = json.loads(r.text)
print(response)



# curl --user myusername - -data-binary '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", 0.00100000, "donation", "seans outpost"] }' - H 'content-type: text/plain;' http://bitcoinrpc:bitcoinrpc@localhost:7777/


# "curl --data-binary  '{"jsonrpc": "1.0", "id":"curltest", "method": "sendtoaddress", "params": ["mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC", 0.00100000, "donation", "seans outpost"] }' -H 'content-type: text/plain;' http://bitcoinrpc:bitcoinrpc@localhost:7777/"

# from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

# # rpc_user and rpc_password are set in the bitcoin.conf file
# rpc_connection = AuthServiceProxy(
#     "http://bitcoinrpc:bitcoinrpc@127.0.0.1:7777")
# best_block_hash = rpc_connection
# print(rpc_connection.getblock(best_block_hash))

# batch support : print timestamps of blocks 0 to 99 in 2 RPC round-trips:
# commands = [["getblockhash", height] for height in range(100)]
# block_hashes = rpc_connection.batch_(commands)
# blocks = rpc_connection.batch_([["getblock", h] for h in block_hashes])
# block_times = [block["time"] for block in blocks]
# print(block_times)

# electrum payto --testnet "mqP7zQ7cVqaeCbXryhaDgqu8nWwuqdNrmC" 0.1 --unsigned > unsigned.txn
