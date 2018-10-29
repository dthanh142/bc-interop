from iota import Iota
from iota import Address, ProposedTransaction, Tag, Transaction, TryteString

# Generate a random seed.

ADDRESS_WITH_CHECKSUM_SECURITY_LEVEL_2 = b"9TPHVCFLAZTZSDUWFBLCJOZICJKKPVDMAASWJZNFFBKRDDTEOUJHR9JVGTJNI9IYNVISZVXARWJFKUZWC"

api = Iota('http://cryptoiota.win:14265', testnet=True)



# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/addresses.rst"


# print(api.get_node_info())
# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/types.rst"

# Generate 1 address, starting with index 42:
gna_result = api.get_new_addresses(index=42, security_level=2, checksum=True)
addresses = gna_result['addresses']
print(addresses)



api.send_transfer(
    depth=100,
    transfers=[
        ProposedTransaction(
            # Recipient of the transfer.
            address=Address(
                'GVMOWHRPLRAQMTMDWKDFNGOCLRYHPHWUSYOTSUUSVVEXLZCHFYANXERRPJPOAVSXEPSTUNEOHIFQYZSEYRNUANOMYA'
            ),
            value=0,
            # Optional tag to attach to the transfer.
            tag=Tag(b'ADAPT'),
            # Optional message to include with the transfer.
            message=TryteString.from_string("Hello!"),
        ),
    ],
)
