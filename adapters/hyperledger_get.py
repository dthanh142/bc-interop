import requests
import json
import base64
import cbor
import colorlog

id="fe121c637858f283b9abf3518631c3b3ed88c34d7f1db4eb6f2205826cfc873464db47e4c1c5a249fd2ae20146142c0ad9db0c39143cad3e9af0794815ce1e3e"

r = requests.get(
    f'http://localhost:8008/batches/{id}',
)
response = json.loads(r.text)
print(f"response: {response['data']['header']['transaction_ids'][0]}")
