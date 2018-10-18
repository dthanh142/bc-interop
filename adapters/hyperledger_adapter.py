import sawtooth_sdk
import cbor
from hashlib import sha512
from sawtooth_sdk.protobuf.transaction_pb2 import TransactionHeader
from sawtooth_sdk.protobuf.transaction_pb2 import Transaction
from sawtooth_sdk.protobuf.batch_pb2 import BatchHeader
import urllib.request
from urllib.error import HTTPError
from sawtooth_sdk.protobuf.batch_pb2 import BatchList
from sawtooth_sdk.protobuf.batch_pb2 import Batch
from sawtooth_signing import create_context
from sawtooth_signing import CryptoFactory



class HyperledgerAdapter():
	context = create_context('secp256k1')
	private_key = context.new_random_private_key()
	signer = CryptoFactory(context).new_signer(private_key)
	# ---Store---
	@classmethod
	def create_transaction(cls, text):
		#encode the payload
		payload = {
		 'Verb': 'set',
		 'Name': text,
		 'Value': 42
		}
		payload_bytes = cbor.dumps(payload)

		#create the transaction header:
		txn_header_bytes = TransactionHeader(
		 family_name='intkey',
		 family_version='1.0',
		 inputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
		 outputs=['1cf1266e282c41be5e4254d8820772c5518a2c5a8c0c7f7eda19594a7eb539453e1ed7'],
		 signer_public_key=cls.signer.get_public_key().as_hex(),
		 # In this example, we're signing the batch with the same private key,
		 # but the batch can be signed by another party, in which case, the
		 # public key will need to be associated with that key.
		 batcher_public_key=cls.signer.get_public_key().as_hex(),
		 # In this example, there are no dependencies.  This list should include
		 # an previous transaction header signatures that must be applied for
		 # this transaction to successfully commit.
		 # For example,
		 # dependencies=['540a6803971d1880ec73a96cb97815a95d374cbad5d865925e5aa0432fcf1931539afe10310c122c5eaae15df61236079abbf4f258889359c4d175516934484a'],
		 dependencies=[],
		 payload_sha512=sha512(payload_bytes).hexdigest()
		   ).SerializeToString()

		return {
			'txn_header_bytes': txn_header_bytes,
			'payload_bytes': payload_bytes,
		   }


	@classmethod
	def sign_transaction(cls, tx_dict):
		signature = cls.signer.sign(tx_dict.get('txn_header_bytes'))
		txn = Transaction(
		 header=tx_dict.get('txn_header_bytes'),
		 header_signature=signature,
		 payload=tx_dict.get('payload_bytes')
		   )
		return txn

	@classmethod
	def send_raw_transaction(cls, txn):
		#create batch header
		txns = [txn]
		batch_header_bytes = BatchHeader(
		 signer_public_key=cls.signer.get_public_key().as_hex(),
		 transaction_ids=[txn.header_signature for txn in txns],
		   ).SerializeToString()
		#create the batch
		signature = cls.signer.sign(batch_header_bytes)
		batch = Batch(
		 header=batch_header_bytes,
		 header_signature=signature,
		 transactions=txns
		   )
		#encode the batch in a batchlist
		batch_list_bytes = BatchList(batches=[batch]).SerializeToString()

		#Submitting Batches to the Validator
		try:
			request = urllib.request.Request(
			 'http://rest.api.domain/batches',
			 batch_list_bytes,
			 method='POST',
			 headers={'Content-Type': 'application/octet-stream'})
			response = urllib.request.urlopen(request)
			print(f"response: {response}")

		except HTTPError as e:
			response = e.file


	@staticmethod
	def add_transaction_to_database(transaction_hash):
		return ""

# ---Retrieve---
	@classmethod
	def get_transaction(cls, transaction_hash):
		return ""

	@staticmethod
	def extract_data(transaction):
		return "transaction.get('memo')"

	@staticmethod
	def to_text(data):
		return str(data)
