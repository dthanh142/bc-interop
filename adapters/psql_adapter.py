import psycopg2
from blockchain import Blockchain
import db.database as database

# from adapters.adapter import Adapter


class PostgresAdapter():
    credentials = database.find_credentials(Blockchain.POSTGRES)
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
            """CREATE TABLE IF NOT EXISTS test (id SERIAL PRIMARY KEY, value text)"""
        )
        connection.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error while connecting to PostgreSQL", error)

    @classmethod
    def retrieve(cls, transaction_hash):
        """Get the transaction data from a tx hash:
        Args:
            param1 (str): The transaction hash.
        Returns:
            string: The transaction data as text.
        """
        # transaction = cls.get_transaction(transaction_hash)
        # data = cls.extract_data(transaction)
        # return cls.to_text(data)

    @classmethod
    def store(cls, text):
        """Store a text in the database:
        Args:
            string: The text to store.
        Returns:
            string: The transaction hash.
        """
        transaction = cls.create_transaction(text)
        print(f"this is the transaction {transaction}")
        transaction_hash = cls.send_raw_transaction(transaction)
        print(transaction_hash)

        #
        # cur.execute("SELECT * FROM test")
        # items = cur.fetchall()

        # cls.add_transaction_to_database(transaction_hash)
        # return transaction_hash

    @staticmethod
    def create_transaction(text):
        query = """INSERT INTO test (id, value) VALUES (DEFAULT, 'TESTVALUE')"""
        return query


    @classmethod
    def send_raw_transaction(cls, transaction):
        try:
            cls.cursor.execute(transaction)
            cls.connection.commit()
            
        except (Exception, psycopg2.DatabaseError) as error:
            print(f"Error while sending transaction: {error}")

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        #SELECT
        #md5(CAST((f.*)AS text))
        #FROM
        #foo f;
        raise NotImplementedError


test = PostgresAdapter()