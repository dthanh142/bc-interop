from enum import Enum, auto


class Blockchain(Enum):
    ETHEREUM = auto()
    MULTICHAIN = auto()
    BITCOIN = auto()
    POSTGRES = auto()
    STELLAR = auto()
    HYPERLEDGER = auto()


def blockchain(blockchain, name):
    return {'blockchain': blockchain, 'name': name}
