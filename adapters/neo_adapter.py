import database
from neorpc.Client import RPCClient
from adapters.adapter import Adapter
from blockchain import Blockchain

class CustomRPCSettings:
	def __init__(self):
		self.RPC_LIST = ["http://localhost:30333"]

class NEOAdapter():	
    client = RPCClient(CustomRPCSettings(), True)
    credentials = database.find_credentials(Blockchain.NEO)
    address = credentials['address']
    key = credentials['key']

    def get_transaction(cls, transaction_hash):
        return cls.client.get_transaction(transaction_hash)
