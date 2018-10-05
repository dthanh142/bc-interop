import database
from neorpc.Client import RPCClient
from adapters.adapter import Adapter
from blockchain import Blockchain

class CustomRPCSettings:
	def __init__(self):
		self.RPC_LIST = ["http://localhost:30333"]

class NEOAdapter(Adapter):	
    client = RPCClient(CustomRPCSettings(), True)
    credentials = database.find_credentials(Blockchain.NEO)
    address = credentials['address']
    key = credentials['key']

    @classmethod
    def get_transaction(cls, transaction_hash):
        return cls.client.get_transaction(transaction_hash)

    # @staticmethod
    # def extract_data(transaction):
    #     # Note that 'input' might be replaced with 'data' in a future release,
    #     # see here for more detailed information:
    #     # https://github.com/ethereum/web3.py/issues/901
    #     return transaction.input

    # @staticmethod
    # def to_text(data):
    #     return Web3.toText(data)

    # @classmethod
    # def create_transaction(cls, text):
    #     # Need to wait until this is implemented see:
    #     # https://github.com/CityOfZion/neo-python/issues/189
    #     pass

    # @classmethod
    # def get_transaction_count(cls):
    #     return cls.client.getTransactionCount(cls.address)

    # @classmethod
    # def estimate_gas(cls, transaction):
    #     return cls.client.get_block_sysfee(height)

    # @classmethod
    # def sign_transaction(cls, transaction):
    #     signed = cls.client.signTransaction(transaction, cls.key)
    #     return signed.rawTransaction

    # @classmethod
    # def send_raw_transaction(cls, transaction):
    #     transaction_hash = cls.client.sendRawTransaction(transaction)
    #     return transaction_hash.hex()

    # @staticmethod
    # def add_transaction_to_database(transaction_hash):
    #     database.add_transaction(transaction_hash, Blockchain.NEO)