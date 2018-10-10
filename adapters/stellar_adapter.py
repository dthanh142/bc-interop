import psycopg2
from blockchain import Blockchain
import db.database as database
from adapters.adapter import Adapter

# TODO: Close connections after doing stuff. At the moment there is only one instance so this is not possible.
# Maybe look for an alternative solution in the future or just leave it like this.


class StellarAdapter(Adapter):

    credentials = database.find_credentials(Blockchain.STELLAR)

    @property
    def address(self):
        raise NotImplementedError

    @property
    def key(self):
        raise NotImplementedError

    try:
        # connect and print version or error
        connection = psycopg2.connect(
            user=credentials['user'],
            password=credentials['password'],
            host="localhost",
            port=credentials['key'],
            database=credentials['address'])
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"Connected to {version}")
        # create table if not exists
        cursor.execute(
            '''CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, value text)'''
        )
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    # ---Store---
    @staticmethod
    def create_transaction(text):
        query = f'''INSERT INTO test (id, value) VALUES (DEFAULT, '{text}') RETURNING id'''
        return query

    @staticmethod
    def sign_transaction(transaction):
        # Not required in case of DB
        return transaction

    @classmethod
    def send_raw_transaction(cls, transaction):
        try:
            cls.cursor.execute(transaction)
            cls.connection.commit()
            return cls.cursor.fetchone()[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error while sending transaction: {error}")

        # finally:
        #     if (cls.connection):
        #         cls.cursor.close()
        #         cls.connection.close()
        #         print("PostgreSQL connection was closed")

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        database.add_transaction(transaction_hash, Blockchain.POSTGRES)

    # ---Retrieve---
    @classmethod
    def get_transaction(cls, transaction_hash):
        try:
            query = f"select value from test WHERE id = {transaction_hash}"
            cls.cursor.execute(query)
            return cls.cursor.fetchone()[0]

        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error while sending transaction: {error}")

        # finally:
        #     if (cls.connection):
        #         cls.cursor.close()
        #         cls.connection.close()
        #         print("PostgreSQL connection was closed")

    @staticmethod
    def extract_data(transaction):
        # Not required in case of DB
        return transaction

    @staticmethod
    def to_text(data):
        return str(data)
