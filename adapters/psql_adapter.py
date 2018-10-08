import psycopg2
from blockchain import Blockchain
import database

# from adapters.adapter import Adapter


class PostgresAdapter():
    credentials = database.find_credentials(Blockchain.POSTGRES)
    try:
        # connect and print version or error
        connection = psycopg2.connect(
            user="test",
            password="123456",
            host="localhost",
            port="5000",
            database="test")
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("Successfully connected to - ", record, "\n")
        # create table if not exists
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS test(id SERIAL PRIMARY KEY, text varchars)"""
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
        print("store was run with text" + text)
        # transaction = cls.create_transaction(text)

        # query = """ INSERT INTO test (name, email) VALUES ('Bobby','bob@b.ch') """
        # cursor.execute(query)
        # con.commit()
        # cur.execute("SELECT * FROM test")
        # items = cur.fetchall()

        # signed_transaction = cls.sign_transaction(transaction)
        # transaction_hash = cls.send_raw_transaction(signed_transaction)
        # cls.add_transaction_to_database(transaction_hash)
        # return transaction_hash

    @classmethod
    def create_transaction(cls, text):
        return f""" INSERT INTO {cls.tableName} (id, value) VALUES (1,{name},'bob@b.ch') """

    @staticmethod
    def sign_transaction(transaction):
        raise NotImplementedError

    @staticmethod
    def send_raw_transaction(transaction):
        raise NotImplementedError

    @staticmethod
    def add_transaction_to_database(transaction_hash):
        #SELECT
        #md5(CAST((f.*)AS text))
        #FROM
        #foo f;
        raise NotImplementedError


test = PostgresAdapter()