#append the root project path to the pythonpath so that blockchain.py can be accessed
import sys, os
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
import sys, os


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

print(store("timsakldjfadsfljlsdkflkjalsdjfljasjfothe", Blockchain.MULTICHAIN))
# print(
#     retrieve(
#         "311b3e771be3efddc31093d19bfddf5d0a894265d1027dd4a5a55f07da42d549"
#     ))
