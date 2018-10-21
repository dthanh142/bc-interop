from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory

context = create_context('secp256k1')
private_key = context.new_random_private_key()
signer = CryptoFactory(context).new_signer(private_key)

import cbor

payload = {'Verb': 'inc', 'Name': 'foo', 'Value': 42}

payload_bytes = cbor.dumps(payload)

from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader



txn_header_bytes = TransactionHeader(
 family_name='intkey',
 family_version='1.0',
 inputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
 outputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
 signer_public_key=signer.get_public_key().as_hex(),
 batcher_public_key=signer.get_public_key().as_hex(),
 dependencies=[],
 payload_sha512=sha512(payload_bytes).hexdigest()
).SerializeToString()

from sawtooth_sdk.protobuf.transaction_pb2 import Transaction

header_signature = signer.sign(txn_header_bytes)

txn = Transaction(
    header=txn_header_bytes,
    header_signature=header_signature,
    payload=payload_bytes)

from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader

txns = [txn]

batch_header_bytes = BatchHeader(
 signer_public_key=signer.get_public_key().as_hex(),
 transaction_ids=[txn.header_signature for txn in txns],
).SerializeToString()

from sawtooth_sdk.protobuf.batch_pb2 import Batch

signature = signer.sign(batch_header_bytes)

batch = Batch(
 header=batch_header_bytes,
 header_signature=signature,
 transactions=txns
)

from sawtooth_sdk.protobuf.batch_pb2 import BatchList

batch_list_bytes = BatchList(batches=[batch]).SerializeToString()

from urllib.error import HTTPError
import requests
import json

try:
    r=requests.post(
     'http://localhost:8008/batches',
     batch_list_bytes,
     headers={'Content-Type': 'application/octet-stream'})
    response = json.loads(r.text)
    print(f"response: {response}")

except HTTPError as e:
    response = e.file
