import psycopg2


class PostgresAdapter(Adapter):
	address = "asdfsaf"
	con = psycopg2.connect(
	    "dbname='test' user='test' host='localhost' password='123456' port=5000")
	cur = con.cursor()
	cur.execute(
	    "CREATE TABLE test(id serial PRIMARY KEY, name varchar, email varchar)")
	con.commit()

	@classmethod
	def retrieve(cls, transaction_hash):
		"""Get the transaction data from a tx hash:
        Args:
            param1 (str): The transaction hash.
        Returns:
            string: The transaction data as text.
        """
		transaction = cls.get_transaction(transaction_hash)
		data = cls.extract_data(transaction)
		return cls.to_text(data)

	@classmethod
	def store(cls, text):
        transaction = cls.create_transaction(text)
        signed_transaction = cls.sign_transaction(transaction)
        transaction_hash = cls.send_raw_transaction(signed_transaction)
        cls.add_transaction_to_database(transaction_hash)
        return transaction_hash

    @staticmethod
    @abstractmethod
    def create_transaction(text):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def sign_transaction(transaction):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def send_raw_transaction(transaction):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def add_transaction_to_database(transaction_hash):
        raise NotImplementedError
