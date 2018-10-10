# from blockchain import Blockchain
# import db.database as database
# from adapters.adapter import Adapter
from stellar_base.keypair import Keypair
from stellar_base.address import Address
from stellar_base.keypair import Keypair
from stellar_base.asset import Asset
from stellar_base.operation import Payment
from stellar_base.transaction import Transaction
from stellar_base.transaction_envelope import TransactionEnvelope as Te
from stellar_base.memo import TextMemo
from stellar_base.horizon import horizon_testnet, horizon_livenet

horizon = horizon_testnet()
# horizon = horizon_livenet() for LIVENET

# create op
amount = '100'
asset = Asset('CNY', CNY_ISSUER)
op = Payment(
    # Source is also inferred from the transaction source, so it's optional.
    source=alice_kp.address().decode(),
    destination=bob_address,
    asset=asset,
    amount=amount)
# create a memo
msg = TextMemo('For beers yesterday!')

# Get the current sequence of Alice
# Python 3
sequence = horizon.account(alice_kp.address().decode('utf-8')).get('sequence')

# Construct a transaction
tx = Transaction(
    source=alice_kp.address().decode(),
    sequence=sequence,
    # time_bounds = {'minTime': 1531000000, 'maxTime': 1531234600},
    memo=msg,
    fee=100,  # Can specify a fee or use the default by not specifying it
    operations=[
        op,
    ],
)

# Build transaction envelope
envelope = Te(tx=tx, network_id="TESTNET")  # or 'PUBLIC'

# Sign the envelope
envelope.sign(alice_kp)

# Submit the transaction to Horizon!
xdr = envelope.xdr()
response = horizon.submit(xdr)
import requests


class StellarAdapter():

    @classmethod
    def createAccount(cls):
        cls.kp = Keypair.random()
        cls.public_key = cls.kp.address().decode()
        cls.private_key = cls.kp.seed().decode()
        print(f"...public key created: {cls.public_key}")
        print(f"...private key created: {cls.private_key}")
        url = 'https://friendbot.stellar.org'
        r = requests.get(url, params={'addr': cls.public_key})

    @classmethod
    def getAccountBalance(cls):
        address = Address(address=cls.public_key)  # See signature for additional args
        address.get()  # Get the latest information from Horizon
        print('Balances: {}'.format(address.balances))

adpt = StellarAdapter()
adpt.createAccount()
adpt.getAccountBalance()


# TODO: Close connections after doing stuff. At the moment there is only one instance so this is not possible.
# Maybe look for an alternative solution in the future or just leave it like this.

# from stellar_base.builder import Builder

# alice_secret = 'SCB6JIZUC3RDHLRGFRTISOUYATKEE63EP7MCHNZNXQMQGZSLZ5CNRTKK'
# bob_address = 'GA7YNBW5CBTJZ3ZZOWX3ZNBKD6OE7A7IHUQVWMY62W2ZBG2SGZVOOPVH'

# builder = Builder(secret=alice_secret)
# builder.add_text_memo("Hello, Stellar!").append_payment_op(destination=bob_address, amount='10.25', asset_code='XLM')
# builder.sign()
# response = builder.submit()
# print(response)

# class StellarAdapter(Adapter):

#     credentials = database.find_credentials(Blockchain.STELLAR)
#     address = credentials['address']
#     key = credentials['key']
#     client =

#     @property
#     def address(self):
#         raise NotImplementedError

#     @property
#     def key(self):
#         raise NotImplementedError

#     try:
#         # connect and print version or error
#         connection = psycopg2.connect(
#             user=credentials['user'],
#             password=credentials['password'],
#             host="localhost",
#             port=credentials['key'],
#             database=credentials['address'])
#         cursor = connection.cursor()
#         cursor.execute("SELECT version();")
#         version = cursor.fetchone()
#         print(f"Connected to {version}")
#         # create table if not exists
#         cursor.execute(
#             '''CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, value text)'''
#         )
#         connection.commit()
#     except (Exception, psycopg2.DatabaseError) as error:
#         print("Error while connecting to PostgreSQL", error)

#     # ---Store---
#     @staticmethod
#     def create_transaction(text):
#         query = f'''INSERT INTO test (id, value) VALUES (DEFAULT, '{text}') RETURNING id'''
#         return query

#     @staticmethod
#     def sign_transaction(transaction):
#         # Not required in case of DB
#         return transaction

#     @classmethod
#     def send_raw_transaction(cls, transaction):
#         try:
#             cls.cursor.execute(transaction)
#             cls.connection.commit()
#             return cls.cursor.fetchone()[0]

#         except (Exception, psycopg2.DatabaseError) as error:
#             print(f"Error while sending transaction: {error}")

#         # finally:
#         #     if (cls.connection):
#         #         cls.cursor.close()
#         #         cls.connection.close()
#         #         print("PostgreSQL connection was closed")

#     @staticmethod
#     def add_transaction_to_database(transaction_hash):
#         database.add_transaction(transaction_hash, Blockchain.POSTGRES)

#     # ---Retrieve---
#     @classmethod
#     def get_transaction(cls, transaction_hash):
#         try:
#             query = f"select value from test WHERE id = {transaction_hash}"
#             cls.cursor.execute(query)
#             return cls.cursor.fetchone()[0]

#         except (Exception, psycopg2.DatabaseError) as error:
#             print(f"Error while sending transaction: {error}")

#         # finally:
#         #     if (cls.connection):
#         #         cls.cursor.close()
#         #         cls.connection.close()
#         #         print("PostgreSQL connection was closed")

#     @staticmethod
#     def extract_data(transaction):
#         # Not required in case of DB
#         return transaction

#     @staticmethod
#     def to_text(data):
#         return str(data)
