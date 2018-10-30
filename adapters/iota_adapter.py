from iota import Iota
from iota import Address, ProposedTransaction, Tag, Transaction, TryteString, TransactionHash
from iota import Bundle

# Generate a random seed.

# ADDRESS_WITH_CHECKSUM_SECURITY_LEVEL_2 = b"9TPHVCFLAZTZSDUWFBLCJOZICJKKPVDMAASWJZNFFBKRDDTEOUJHR9JVGTJNI9IYNVISZVXARWJFKUZWC"

api = Iota('https://nodes.devnet.iota.org:443', testnet=True)


def get_tx():
    # txhash = TransactionHash.from_string(
    #     "CFXVRNNIVJTONAAUVLVKVTJUAJVHNIIC9TYSZLHECWNANLMNGKTVBL9NKWGOSMZJHGUTGBMHSEYGSW999")
    # txstring = TryteString.from_string(
    #     "CFXVRNNIVJTONAAUVLVKVTJUAJVHNIIC9TYSZLHECWNANLMNGKTVBL9NKWGOSMZJHGUTGBMHSEYGSW999")
    return api.get_bundles("CFXVRNNIVJTONAAUVLVKVTJUAJVHNIIC9TYSZLHECWNANLMNGKTVBL9NKWGOSMZJHGUTGBMHSEYGSW999")
# bundle = get_tx()["bundles"]
# print(Bundle.as_json_compatible(bundle))
# # print("test:")
# # print(b'999999999999999999999999999999999999999999999999999999999999999999999999999999999')

# print(bundle.get_messages())






# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/addresses.rst"

print(api.get_node_info())
# "https://github.com/iotaledger/iota.lib.py/blob/master/docs/types.rst"

# Generate 1 address, starting with index 42:


# https://medium.com/coinmonks/exploring-iota-2-retrieve-your-transaction-and-create-your-wallet-bc8e8c91fec9

def create_address():
    gna_result = api.get_new_addresses(index=42, security_level=2, checksum=True)
    addresses = gna_result['addresses']
    print(addresses)

def transfer():
    # "https://pyota.readthedocs.io/en/latest/api.html#send-transfer"
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

# Transaction.
# print(TryteString.decode())

# transfer()


# CFXVRNNIVJTONAAUVLVKVTJUAJVHNIIC9TYSZLHECWNANLMNGKTVBL9NKWGOSMZJHGUTGBMHSEYGSW999




# trytes = 'HELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDHELLOWORLDD'

# message = api.utils.toTrytes('Hello Jan, this is your first transaction!')



# const transfers = [{
#     value: 0,
#     address: trytes,
#     message: message
# }]

# iota.api.sendTransfer(trytes, 3, 9, transfers, (error, success)=> {
#     if (error) {
#         console.log(error)
#     } else {
#         console.log(success)
#     }
# })
