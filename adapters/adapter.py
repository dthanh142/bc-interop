from abc import ABC, abstractmethod
import db.database as db
from db.config import CONFIRMATION_WAITING_TIMES, WAIT_FOR_CONFIRMATION
import time


class Adapter(ABC):

    @property
    @abstractmethod
    def credentials(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def address(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def key(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def client(self):
        raise NotImplementedError

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

    @staticmethod
    @abstractmethod
    def get_transaction(transaction_hash):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def extract_data(transaction):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def to_text(data):
        raise NotImplementedError

    @classmethod
    def store(cls, text):
        transaction = cls.create_transaction(text)
        signed_transaction = cls.sign_transaction(transaction)
        transaction_hash = cls.send_raw_transaction(signed_transaction)
        if(WAIT_FOR_CONFIRMATION):
            if(cls.confirmation_check(transaction_hash)):
                cls.add_transaction_to_database(transaction_hash)
                return transaction_hash
            else:
                raise LookupError(
                    'Transaction was not confirmed and therefore not added in DB')
        else:
            cls.add_transaction_to_database(transaction_hash)
            return transaction_hash


    @classmethod
    def confirmation_check(cls, transaction_hash):
        bc_id = cls.chain.value
        waiting_time = CONFIRMATION_WAITING_TIMES[bc_id]
        time.sleep(waiting_time)
        value = cls.retrieve(transaction_hash)
        if(type(value) == str):
            return True
        else:    
            return False

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
