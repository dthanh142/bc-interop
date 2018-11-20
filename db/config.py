from blockchain import Blockchain

AMOUNT = 0
ENCODING = 'utf-8'
DATABASE_PATH = 'db/bcio.db'

CREDENTIALS = [
    {
        "blockchain" : Blockchain.ETHEREUM.name,
        "id": Blockchain.ETHEREUM.value,
        "address" : '0xf717e2d05037d13d6bfd0d783d6f4ebd68dd5b46',
        "key" : '0xec7a5eb646075cc16dd842381489614a49eda87e1f600d8780bbb3012288a98f',
        "user" : 'ethereum (not used)',
        "password" : 'ethereum (not used)',
    },
    {
        "blockchain" : Blockchain.MULTICHAIN,
        "id": Blockchain.MULTICHAIN.value,
        "address" : '1MRQf6mYRDoXjtoKVBi8huxBC69zmSzheYN4yM',
        "key" : 'V7BFGjp4wrowNSJDSouXVFJQkwZxMFDScba4SkHYA9aYjEDhLrFBV2Nd',
        "user" : 'multichainrpc',
        "password" : 'GkHfnch8QBgqvZJeMLyb57h42h6TZREr25Uhp5iZ8T2E'
    },
    {
        "blockchain" : Blockchain.BITCOIN,
        "id": Blockchain.BITCOIN.value,
        "address" : '2NGMq7iBuJTeDMQPxSaEQVqMtdt3VQxuN7B',
        "key" : 'cS6kdk7zxTCij8HpXHE8Kdnh1uAM46PU5LNtQxpBZ6YjP3t3zgWL',
        "user" : 'bitcoinrpc',
        "password" : 'f7efda5c189b999524f151318c0c86$d5b51b3beffbc02b724e5d095828e0bc8b2456e9ac8757ae3211a5d9b16a22ae'
    },
    {
        "blockchain" : Blockchain.POSTGRES,
        "id": Blockchain.POSTGRES.value,
        # database name
        "address" : 'test',
        # port number
        "key" : '5000',
        "user" : 'test',
        "password" : '123456'
    },
    {
        "blockchain" : Blockchain.STELLAR,
        "id": Blockchain.STELLAR.value,
        "address" : 'GCCAETWXN5VYPOU4MYTUGTFPTSWWNFYMDZWHWS566PUXR5GCQ7SY7QHQ',
        "key" : 'SBJF56A62FP7OEATJIDFYUTXORNJXWGXD5GBWW7TDVN2QMHDJMOXBLPK',
        "user" : 'stellar (not used)',
        "password" : 'stellar (not used)'
    },
    {
        "blockchain" : Blockchain.HYPERLEDGER,
        "id": Blockchain.HYPERLEDGER.value,
        "address" : 'will be generated from private key',
        "key" : 'c2d0a398c3c3074e066b953b3bb15ae7053fd8aba1c2279b2f3ff058ab7e7661',
        "user" : 'hyperledger (not used)',
        "password" : 'hyperledger (not used)'
    },
    {
        "blockchain" : Blockchain.EOS,
        "id": Blockchain.EOS.value,
        "address" : 'EOS8Vfg6ssQxj66wX9LrFq3EZY8z4EEkiyiQiDc7bwyn65K4YFVwW',
        "key" : '5KazRYnXDCNougrvuVtZFDMAiB3kr7M2tjGYNJtQQ2Wn3JFRdTM',
        "user" : 'jungletimohe',
        "password" : 'eos (not used)'
    },
    {
        "blockchain" : Blockchain.IOTA,
        "id": Blockchain.IOTA.value,
        "address" : 'GVMOWHRPLRAQMTMDWKDFNGOCLRYHPHWUSYOTSUUSVVEXLZCHFYANXERRPJPOAVSXEPSTUNEOHIFQYZSEYRNUANOMYA',
        "key" : 'iota (not used)',
        "user" : 'iota (not used)',
        "password" : 'iota (not used)',
    }
]
TRANSACTIONS = [
    {
        "blockchain": Blockchain.MULTICHAIN.value,
        "transaction_hash": '826e7100deeef7def0bfed7f5160ae6ac55a3a0cc8fca660a30488c1755e370d',
    },
    {
        "blockchain": Blockchain.BITCOIN.value,
        "transaction_hash": '151d65141a9a4a9c37fc0c8ac7aa23feb0981876b8198a970fb9956ca34e467c',
    }
]
