# Setup

## Python

Install the following packages using your favourite package manager:

```console
# pacman -S python python-pip
```

### With virtual environment

Create a virtual environment within the project (for `python >= 3.3`):

```console
$ python -m venv venv
```

Activate virtual environment:

```console
$ source venv/bin/activate
```

Install dependencies:

```
(venv) $ pip install web3 mcrpc python-bitcoinrpc
```

Deactivate virtual environment:

```
(venv) $ deactivate
```

### Without virtual environment

Install dependencies:

```console
$ pip install --user web3 mcrpc python-bitcoinrpc
```

## Database

Install the following package using your favourite package manager:

```console
# pacman -S sqlite
```

Run the database setup:

```python
import database
database.setup()
```

> Calling the `setup` function of the [`database`](database.py) module will:
>
> 1. drop `credentials` and `transactions` tables if they already exist
> 2. create tables for storing `credentials` and `transactions`
> 3. seed the `credentials` table with credentials for Ethereum, MultiChain and Bitcoin
> 4. seed the `transactions` table with input transactions for MultiChain and Bitcoin

> Seed values are read from the [`config`](config.py) module.

## Ethereum

This command will start a docker node with a preconfigured account which holds 100 eth
`docker-compose -f  docker/docker_compose_eth.yaml up`

### Dependencies
Docker image used from here:    
https://hub.docker.com/r/trufflesuite/ganache-cli/

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

##NEO

https://neo-python.readthedocs.io/en/latest/

This currently only works with python 3.6, not the current 3.7    
see https://github.com/CityOfZion/neo-python/issues/518

List of possible RPC actions:
http://docs.neo.org/en-us/node/cli/2.9.0/api.html

use privateNet with docker image:    
https://hub.docker.com/r/cityofzion/neo-privatenet/

Python RPC
https://github.com/CityOfZion/neo-python-rpc

(1) Install level db:    
`brew install leveldb`

(2) Install neo python:    
`pip install neo-python`

(3) Bootstrap the Testnet (Mainnet)    
`np-bootstrap` (`np-bootstrap -m`)

(4) Create a wallet and unlock (open it):    
`create wallet {wallet_path}`
`open wallet {wallet_path}`

(5) Start the rest and rpc server:      
`np-api-server --testnet --port-rpc 10332 --port-rest 80`

##Postgres Database
(1) Install Docker
(2) Pull the postgres image with `docker pull postgres`
(3) Run a postgres server in a docker container `docker run --name postgres -e POSTGRES_PASSWORD=123456 -e POSTGRES_USER=test -p 127.0.0.1:5000:5432 -d postgres` The database will be reachable under localhost:5000
(4) 

Sources:    
Psycopg: http://initd.org/psycopg/docs/install.html#binary-install-from-pypi
https://pynative.com/python-postgresql-tutorial/


##Stellar
Install the stellar sdk:    
`pip install stellar-sdk`


###Run with local node
Run a docker container and map port 8000 for REST requests.    
`docker run --rm -it -p "8000:8000" --name stellar stellar/quickstart --testnet`    
In stellar_adapter.py, enable the following line:   
builder = Builder(secret=cls.key, horizon_uri="http://localhost:8000/")

Sources:     
Horizon server on docker: https://hub.docker.com/r/stellar/quickstart/    
Python SDK to interact with horizon: https://github.com/StellarCN/py-stellar-base          
API documentation: https://stellar-base.readthedocs.io/en/latest/api.html    

Maximum size to save on stellar is 28 bytes.    
https://www.stellar.org/developers/guides/concepts/transactions.html#memo    

##Hyperledger Sawtooth
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
download and unpack: https://pypi.org/project/sawtooth-sdk/#files
cd in the folder and run `python setup.py install`


## EOS
1. `pip install git+https://github.com/EvaCoop/eosjs_python.git` (Until my changes are published to pip)
2. `cd venv/lib/python3.6/site-packages/eosjs_python/js && npm i --save eosjs@16.0.9`
3. create an account on the jungle testnet using http://jungle.cryptolions.io/#home