# from adapters.eth_adapter import EthAdapter
# from adapters.mc_adapter import MCAdapter
# from adapters.btc_adapter import BTCAdapter
# from adapters.psql_adapter import PostgresAdapter
from adapters.stellar_adapter import StellarAdapter
from blockchain import Blockchain
import db.database as database

Adapter = {
    # Blockchain.ETHEREUM: EthAdapter,
    # Blockchain.MULTICHAIN: MCAdapter,
    # Blockchain.BITCOIN: BTCAdapter,
    # Blockchain.POSTGRES:
    # PostgresAdapter,
    Blockchain.STELLAR:
    StellarAdapter,
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


# print(store('localhosttest', Blockchain.STELLAR))
print(
    retrieve(
        "412fadb2eedd68420a8175032c0efdebb07799297add072deb7bb97da4c63246"))
