from neorpc.Client import RPCClient

class CustomRPCSettings:
	def __init__(self):
		self.RPC_LIST = ["http://localhost:30333"]

class NEOAdapter(Adapter):	
	settings = CustomRPCSettings()

	client = RPCClient(settings, True)

	# print(client.get_height())
	# raw_tx = '80000120d8edd2df8d6907caacd4af8872a596cb75c5829d015ce72895ce376d12def9a780ba502ae28ad7a4b7fbcf6baa4856edb537417d2a0000029b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500a3e11100000000d8edd2df8d6907caacd4af8872a596cb75c5829d9b7cffdaa674beae0f930ebe6085af9093e5fe56b34a5c220ccdcf6efc336fc500bbeea000000000d8edd2df8d6907caacd4af8872a596cb75c5829d01414044dfd2b360e548607ece3d453173079233040c2484a99671a7346a8ca16969245b946bfa4c13125f4c931b0cbab216e0d241d908f37ad96abb776890832a3a4b2321025de86902ed42aca7246207a70869b22253aeb7cc84a4cb5eee3773fd78b3f339ac'
# print(client.)
    credentials = database.find_credentials(Blockchain.ETHEREUM)
    address = credentials['address']
    if not Web3.isChecksumAddress(address):
        address = Web3.toChecksumAddress(address)
    key = credentials['key']
    web3 = Web3(HTTPProvider(ENDPOINT_URI))
    client = web3.eth

    @classmethod
    def get_transaction(cls, transaction_hash):
        return cls.client.getTransaction(transaction_hash)

    @staticmethod
    def extract_data(transaction):
        # Note that 'input' might be replaced with 'data' in a future release,
        # see here for more detailed information:
        # https://github.com/ethereum/web3.py/issues/901
        return transaction.input

    @staticmethod
    def to_text(data):
        return Web3.toText(data)

    @classmethod
    def create_transaction(cls, text):
        transaction = {
            'from': cls.address,
            'to': cls.address,
            'gasPrice': cls.client.gasPrice,
            'value': AMOUNT,
            'data': bytes(text, ENCODING),
            'nonce': cls.get_transaction_count()
        }
        transaction['gas'] = cls.estimate_gas(transaction)
        return transaction

    @classmethod
    def get_transaction_count(cls):
        return cls.client.getTransactionCount(cls.address)

    @classmethod
    def estimate_gas(cls, transaction):
        return cls.client.estimateGas(transaction)

    @classmethod
    def sign_transaction(cls, transaction):
        signed = cls.client.account.signTransaction(transaction, cls.key)
        return signed.rawTransaction

    @classmethod
    def send_raw_transaction(cls, transaction):
        transaction_hash = cls.client.sendRawTransaction(transaction)
        return transaction_hash.hex()

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        database.add_transaction(transaction_hash, Blockchain.ETHEREUM)

