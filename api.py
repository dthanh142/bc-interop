# append the root project path to the pythonpath so that blockchain.py can be accessed by every adapter
import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")

# from adapters.btc_adapter import BTCAdapter
from adapters.mc_adapter import MCAdapter
from adapters.eth_adapter import EthAdapter
from adapters.postgres_adapter import PostgresAdapter
from adapters.stellar_adapter import StellarAdapter
from adapters.eos_adapter import EosAdapter
from adapters.iota_adapter import IotaAdapter
from adapters.hyperledger_adapter import HyperledgerAdapter

from blockchain import Blockchain
import db.database as database
import sys
import os
import string
import random


Adapter = {
    # Blockchain.BITCOIN: BTCAdapter,
    Blockchain.MULTICHAIN: MCAdapter,
    Blockchain.ETHEREUM: EthAdapter,
    Blockchain.POSTGRES: PostgresAdapter,
    Blockchain.STELLAR: StellarAdapter,
    Blockchain.EOS: EosAdapter,
    Blockchain.IOTA: IotaAdapter,
    Blockchain.HYPERLEDGER: HyperledgerAdapter

}


def store(text, blockchain):
    """Store a text in a specific Blockchain:
        Args:
            Blockchain to use, e.g. Ethereum.
        Returns:
            string: The transaction hash.
    """
    adapter = Adapter[blockchain]
    transaction_hash = adapter.store(text)
    return transaction_hash


def retrieve(transaction_hash):
    """Get the text stored on the Blockchain:
        Args:
            Transaction hash
        Returns:
            string: The text belonging to the transactiont.
    """
    blockchain = database.find_blockchain(transaction_hash)
    adapter = Adapter[blockchain]
    text = adapter.retrieve(transaction_hash)
    return text


def migrate(transaction_hash, blockchain):
    """Copy a value from a transaction to another Blockchain:
        Args:
            Transaction hash
        Returns:
            string: The transaction hash from the new transaction.
    """
    value = retrieve(transaction_hash)
    new_hash = store(value, blockchain)
    return new_hash


# def make_random_string():
#     # Not working yet
#     base_chars = ['a', 'b', 'c', 'd', 'e', 'f', '1', '2', '3']
#     word_length = 10  # change this to the desired word length
#     print([random.choice(base_chars) for _ in range(word_length)])


print(store("timoishere", Blockchain.MULTICHAIN))


# print(
#     retrieve(
#         "170d2895f0cbd89f9ec55fd3a30baa78d1f0dfc5b0ee3ce84edcf22c568ceebd"
#     ))
# print(migrate("f12cc0275e47d8040c04d0ea0d26bf8117f25e0628697da338f73e1eb3d39cad;25316099",
#         Blockchain.STELLAR))