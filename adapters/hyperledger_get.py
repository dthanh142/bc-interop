import requests
import json
import base64
import cbor
import colorlog



r = requests.get(
    'http://localhost:8008/transactions/4842b2df99eab4bcf34dd522f22dd43da3b090fadc831e20729e0cf98e82ea872dd73d0d202bf83cd56aa36476d46c541530c9a11056c340053556854db64621',
)
response = json.loads(r.text)
print(f"response: {response}")
