from neorpc.Client import RPCClient


class CustomRPCSettings:
	def __init__(self):
		self.RPC_LIST = ["http://localhost:30333"]

class NEOAdapter():	
    client = RPCClient(CustomRPCSettings(), True)
    client.
    
    @classmethod
    def get_account(cls):
        acc = cls.client.get_account("AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y")
        print(f"This is the account: {acc}")

    @classmethod
    def make_transaction(cls):
        tx = "bla"
        cls.client.send_raw_tx(tx)


   



