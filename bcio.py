# from adapters.eth_adapter import EthAdapter
# from adapters.mc_adapter import MCAdapter
# from adapters.btc_adapter import BTCAdapter
# from adapters.psql_adapter import PostgresAdapter
# from adapters.stellar_adapter import StellarAdapter
from adapters.hyperledger_adapter import HyperledgerAdapter
from blockchain import Blockchain
import db.database as database

Adapter = {
    # Blockchain.ETHEREUM: EthAdapter,
    # Blockchain.MULTICHAIN: MCAdapter,
    # Blockchain.BITCOIN: BTCAdapter,
    # Blockchain.POSTGRES: PostgresAdapter,
    # Blockchain.STELLAR: StellarAdapter,
    Blockchain.HYPERLEDGER: HyperledgerAdapter,
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

# store("ljjkjk", Blockchain.HYPERLEDGER)
print(
    retrieve(
        "73d57d2bfb6c63c3fb48460b254c3ef0b3923995eadbb7b09dfd89ab1b4afc222e2c5a433ce36e74142445d83c771feb014b71b089031febe0fbc8e16ad60818"
    ))
