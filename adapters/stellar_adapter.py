from blockchain import Blockchain
import db.database as database
from adapters.adapter import Adapter
from stellar_base.keypair import Keypair
from stellar_base.address import Address
from stellar_base.asset import Asset
from stellar_base.operation import Payment
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet, horizon_livenet

class StellarAdapter(Adapter):
    client = horizon_testnet()
    # horizon = horizon_livenet() for LIVENET
    credentials = database.find_credentials(Blockchain.STELLAR)
    address = credentials['address']
    key = credentials['key']
    #keypair object instead of individual strings are used by api
    keypair = Keypair.from_seed(key)
    
    # ---Store---
    @classmethod
    def create_transaction(cls, payload):
        op = Payment(
            opts={
                'source':cls.address ,
                'destination':cls.address,
                'asset':'XLM',
                'amount':'1'
        })
        # Construct a transaction
        tx = Transaction(
            source = cls.keypair.address().decode(),
            opts={
                'sequence':cls.client.account(cls.keypair.address().decode('utf-8')).get('sequence'),
                'memo':TextMemo(payload),
                'operations':[op,],
            }
        )
        transaction = TransactionEnvelope(tx=tx)  # or 'PUBLIC'
        return transaction

    @classmethod
    def sign_transaction(cls, transaction):
        transaction = transaction.sign(cls.keypair)
        return transaction

    @classmethod
    def send_raw_transaction(cls, transaction):
        try:
            xdr = transaction.xdr()
            response = cls.client.submit(xdr)
            print(f"this is the response after sending the transaction: {response}")

        except (Exception):
            print(f"Error while sending transaction: {Exception}")

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        database.add_transaction(transaction_hash, Blockchain.STELLAR)

    # ---Retrieve---
    @classmethod
    def get_transaction(cls, transaction_hash):
        try:
            # query = f"select value from test WHERE id = {transaction_hash}"
            # cls.cursor.execute(query)
            # return cls.cursor.fetchone()[0]
            pass

        except (Exception):
            pass
            # print(f"Error while sending transaction: {Exception}")

    @staticmethod
    def extract_data(transaction):
        # Not required in case of DB
        return transaction

    @staticmethod
    def to_text(data):
        return str(data)
