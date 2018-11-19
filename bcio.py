# from adapters.eth_adapter import EthAdapter
from adapters.iota_adapter import IotaAdapter
# from adapters.mc_adapter import MCAdapter
# from adapters.btc_adapter import BTCAdapter
# from adapters.psql_adapter import PostgresAdapter
# from adapters.stellar_adapter import StellarAdapter
# from adapters.hyperledger_adapter import HyperledgerAdapter
from blockchain import Blockchain
import db.database as database
import sys, os

#append the root project path to the pythonpath so that blockchain.py can be accessed
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

Adapter = {
    # Blockchain.ETHEREUM: EthAdapter,
    # Blockchain.MULTICHAIN: MCAdapter,
    # Blockchain.BITCOIN: BTCAdapter,
    # Blockchain.POSTGRES: PostgresAdapter,
    # Blockchain.STELLAR: StellarAdapter,
    # Blockchain.HYPERLEDGER: HyperledgerAdapter,
    Blockchain.IOTA: IotaAdapter
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

# store("test_neuer", Blockchain.IOTA)
print(
    retrieve( 
        "AVSOQXUJEFHIMVYZXAILMDVCKRLFKTDLGMHVHUNFNSWZBIZMRWAXZAAWLZJCFHDFIMFQSMPKVPGTXD999"
    )
)
