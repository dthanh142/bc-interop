from iota import Iota, Address, ProposedTransaction, Tag, Transaction, TryteString, TransactionHash, Bundle

# Generate a random seed.
# ADDRESS_WITH_CHECKSUM_SECURITY_LEVEL_2 = b"9TPHVCFLAZTZSDUWFBLCJOZICJKKPVDMAASWJZNFFBKRDDTEOUJHR9JVGTJNI9IYNVISZVXARWJFKUZWC"
# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/addresses.rst"
# print(api.get_node_info())
# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/types.rst"
# Generate 1 address, starting with index 42:
# https://medium.com/coinmonks/exploring-iota-2-retrieve-your-transaction-and-create-your-wallet-bc8e8c91fec9
# working_tx = "IMLLFGKXGLFFTTAEBQIVFAWTMJVVKONKRXJBYQJDVWIPUYJOSEHYPGF9JAYJXXEIMZFRYBXTPOQWTW999"


def create_address():
    gna_result = api.get_new_addresses(
        index=42, security_level=2, checksum=True)
    addresses = gna_result['addresses']
    print(addresses)
