import requests, json

data = '{"id":"curltext","method":"payto","params":{"destination":"2MwrKtjVPNUAZrHeQskv2TdcFt5AfLhE7kr", "amount":"0.001"}}'




data = {
	"id": "curltext",
	"method": "payto",
   	"params": {"destination": "2MwrKtjVPNUAZrHeQskv2TdcFt5AfLhE7kr", "amount": "0.00010000"}
}
r = requests.post('http://bitcoinrpc:bitcoinrpc@localhost:7777/', json=data)
response = json.loads(r.text)
print (response)

	
