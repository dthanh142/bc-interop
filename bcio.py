from adapters.eth_adapter import EthAdapter
from adapters.mc_adapter import MCAdapter
from adapters.btc_adapter import BTCAdapter
from blockchain import Blockchain
import database

Adapter = {
    Blockchain.ETHEREUM: EthAdapter,
    Blockchain.MULTICHAIN: MCAdapter,
    Blockchain.BITCOIN: BTCAdapter
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

