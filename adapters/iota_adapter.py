import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")
from adapters.adapter import Adapter
from blockchain import Blockchain
# import db.database as database
from iota import Iota, Address, ProposedTransaction, Tag, Transaction, TryteString, TransactionHash, Bundle



class IotaAdapter(Adapter):

    api = Iota('https://nodes.devnet.iota.org:443', testnet=True)
    # credentials = database.find_credentials(Blockchain.STELLAR)
    # address = credentials['address']
    # key = credentials['key']

    # ---Store---
    @classmethod
    def create_transaction(cls, text):
        tx = ProposedTransaction(
            # Recipient
            address=Address(
                'GVMOWHRPLRAQMTMDWKDFNGOCLRYHPHWUSYOTSUUSVVEXLZCHFYANXERRPJPOAVSXEPSTUNEOHIFQYZSEYRNUANOMYA'),
            value=0,
            message=TryteString.from_string(text),
        ),
        return tx

    @staticmethod
    def sign_transaction(tx):
        # tx will be signed and sent in send_raw_transaction
        return tx

    @classmethod
    def send_raw_transaction(cls, tx):
        # "https://pyota.readthedocs.io/en/latest/api.html#send-transfer"
        cls.api.send_transfer(
            depth=4,
            transfers=[tx],
        )
        return hash

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        print(transaction_hash)

    # ---Retrieve---
    @classmethod
    def get_transaction(cls, transaction_hash):
        bundle = cls.api.get_bundles(hash)
        return bundle["bundles"][0]

    @staticmethod
    def extract_data(bundle):
        json = Bundle.as_json_compatible(bundle)
        data = json[0]["signature_message_fragment"]
        return data

    @staticmethod
    def to_text(data):
        data = TryteString.decode(data)
        return str(data)
