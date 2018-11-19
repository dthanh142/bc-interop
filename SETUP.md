# Setup

## Bitcoin

Install the following packages using your favourite package manager:

```console
# pacman -S bitcoind bitcoin-cli
```

> A GUI client is available in `bitcoin-qt`.

### Connecting to the Public Testnet

To connect to the public testnet of Bitcoin (`testnet3`), the following settings are required in the `~/.bitcoin/bitcoin.conf` file:

```
testnet = 1
rpcuser = 'bitcoinrpc'
rpcpassword = 'password'
```

> An example configuration file is available [here](https://github.com/bitcoin/bitcoin/blob/master/contrib/debian/examples/bitcoin.conf).

> In `bitcoind` rpc connections are allowed by default, in `bitcoin-qt` `server = 1` is required in the configuration file to allow rpc connections.

To sync the node with the public testnet:

```console
$ bitcoind
```

The progress of the syncing process can be monitored with:

```console
$ tail -f ~/.bitcoin/testnet3/debug.log
```

To stop the blockchain:

```console
$ bitcoin-cli stop
```


## MultiChain

On Arch Linux, a package is available from the Arch User Repository. Install the following package using your favourite AUR helper:

```console
$ yay -S multichain-alpha
```

### Creating a Private Testnet

First we will create a new blockchain named `chain1`:

```console
$ multichain-util create chain1
```

> The API credentials for the blockchain are stored in the `~/.multichain/chain1/multichain.conf` file.
> The blockchain's settings are stored in the `~/.multichain/chain1/params.dat` file.

> Once the blockchain is initialized, **these parameters cannot be changed**.

Initialize the blockchain, including creating the genesis block:

```console
$ multichaind chain1 -daemon
```

Enter interactive mode:

```console
$ multichain-cli chain1
```

In interactive mode, generate public/private key pairs that are not stored in the wallet or drawn from the node's key pool (for external key management):

```
> createkeypairs

[
    {
        "address" : "1LKfR5yQVKx3YJ27enyKDNske7XFHzkN6bm43Y",
        "pubkey" : "0323187cd83c9dde13f223b5df1fb2899e645e8b0cd1fa73ae61c41b07ce9cd7a6",
        "privkey" : "VHrFLuvdBeb1oVTmKD48Sdm1ovoc8mS5pbrk2gpKhCUWh72LavvAF8jx"
    }
]
```

Before, we can use the generated address in transactions, we have to grant it permission to send and receive within the blockchain:

```
> grant 1LKfR5yQVKx3YJ27enyKDNske7XFHzkN6bm43Y send,receive

ddcca7c4d57bb185443914cdac7a6a9d3b93743d8f39cd61a989b8bdfd09e49b
```

> This command will return a transaction hash (which can be used as seed transaction).

Stop the blockchain:

```
> stop
```


## Ethereum

This command will start a docker node with a preconfigured account which holds 100 eth
`docker-compose -f  docker/docker_compose_eth.yaml up`

### Dependencies
Docker image used from here:    
https://hub.docker.com/r/trufflesuite/ganache-cli/

## Postgres
`docker-compose -f docker/docker_compose_postgres.yaml up`

#### More information:    
Psycopg: http://initd.org/psycopg/docs/install.html#binary-install-from-pypi    
https://pynative.com/python-postgresql-tutorial/


## Stellar
Uses public node, no local node is needed

### To run with local node instead of public node
Run a docker container and map port 8000 for REST requests.    
`docker run --rm -it -p "8000:8000" --name stellar stellar/quickstart --testnet`    
In stellar_adapter.py, enable the following line:   
builder = Builder(secret=cls.key, horizon_uri="http://localhost:8000/")

### Account creation
An account on the testnet can be created by running account_creation/createStellarAccount

### More Information:     
Horizon server on docker: https://hub.docker.com/r/stellar/quickstart/    
Python SDK to interact with horizon: https://github.com/StellarCN/py-stellar-base          
API documentation: https://stellar-base.readthedocs.io/en/latest/api.html    

Maximum size to save on stellar is 28 bytes.    
https://www.stellar.org/developers/guides/concepts/transactions.html#memo    

files
cd in the folder and run `python setup.py install`


## EOS

Uses public node, no local node is needed    

1. `pip install git+https://github.com/EvaCoop/eosjs_python.git` (Until my changes are published to pip)
2. `cd venv/lib/python3.6/site-packages/eosjs_python/js && npm i --save eosjs@16.0.9`

### Account creation
An account can be created using http://jungle.cryptolions.io/#home

## IOTA
Note:  IOTA does not need a sender for zero-value transactions. This means there is no need to create an account and private key to sign the transaction.

## Hyperledger Sawtooth

### Install secp256k1 for Hyperledger installation
Because python 3.6 is not compatible with secp256k1, you need to pull it from another repo and manually install it.    

Make sure those are installed on your machine by running (mac):     
`brew install autoconf automake libtool`

IF there is a certification error installing secp256k1:    
`/Applications/Python\ 3.6/Install\ Certificates.command`

Download the source from the repo:
https://github.com/stfairy/secp256k1-py
cd into this directory and then run `python3 setup.py install` to install secp256k1.     
After that it should be possible to install the hyperledger sawtooth python sdk (`pip install sawtooth-sdk`, will be run from  requirements.txt)

### General setup


https://sawtooth.hyperledger.org/docs/core/releases/1.0/app_developers_guide/docker.html

Start:    
`docker-compose -f setup_helpers/sawtooth-default.yaml up`
Stop:    
`docker-compose -f sawtooth-default.yaml down`
Test if up:    
`curl http://localhost:8008/blocks`

`docker-compose -f /Users/timo/Documents/repos/bc-interop/setup_helpers/sawtooth-default.yaml up`

###Install Python SDK locally

As install with pip fails on any other version except 3.5      
download and unpack: https://pypi.org/project/sawtooth-sdk/#
