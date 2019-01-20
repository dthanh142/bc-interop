# Setup

## General Remarks
The credentials for the test accounts are already provided in the database.

## Bitcoin

Install the following packages using your favourite package manager:

```console
# pacman -S bitcoind bitcoin-cli
```

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

## Ethereum
This command will start a docker node with a preconfigured account which holds 100 eth
`docker-compose -f  docker/docker_compose_eth.yaml up` (on Linux, sudo may be required)

### Dependencies
Docker image used from here:    
https://hub.docker.com/r/trufflesuite/ganache-cli/

## Postgres
This will start a postgres server on docker with the following configuration:
```
User = test
Password = 123456
Port 5432
```
The DB structure will be automatically build when using the adapter.
`docker-compose -f docker/docker_compose_postgres.yaml up`  (on Linux, sudo may be required)

#### More information:    
Psycopg: http://initd.org/psycopg/docs/install.html#binary-install-from-pypi    
https://pynative.com/python-postgresql-tutorial/


## Stellar
Uses public node, no local node is needed

### To run with local node instead of public node
Run a docker container and map port 8000 for REST requests.    
`docker run --rm -it -p "8000:8000" --name stellar stellar/quickstart --testnet`  (on Linux, sudo may be required)   
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
Uses public node, no local node is needed.
The EOS library uses NodeJS in the background. Therefore install NodeJS:    
Mac: https://nodejs.org/en/download/     
Linux:`apt-get -y install nodejs`
Install eosjs with node:    
`sudo npm install -g eosjs`

### Account creation
An account can be created using http://jungle.cryptolions.io/#home

## IOTA
Uses public node, no local node is needed.    
IOTA does not need a sender for zero-value transactions. This means there is no need to create an account and private key to sign the transaction.

## Hyperledger Sawtooth
Start the node:    
`docker-compose -f docker/docker-compose_hyperledger.yaml up`  (on Linux, sudo may be required)    

### Fix Sawtooth SDK installation issues
Sawtooth only supports version 3.5.
Thus, when installing requirements there will be some errors while installing sawtooth-sdk.

#### Linux
`apt-get install autoconf automake libtool`    
`sudo apt install libsecp256k1-dev`    
`sudo apt install python3-pip`    
`sudo -H pip3 install secp256k1`    
`sudo apt-get install libssl-dev`    
`sudo pip3 install sawtooth-sdk`    

See:    
https://github.com/ludbb/secp256k1-py/issues/24#issuecomment-397505150

#### Mac

download and unpack: https://pypi.org/project/sawtooth-sdk/#
Make sure those are installed on your machine by running:         
`brew install autoconf automake libtool`    
IF there is a certification error installing secp256k1:    
`/Applications/Python\ 3.6/Install\ Certificates.command`

Download the source from the repo:
https://github.com/stfairy/secp256k1-py
`sudo apt-get install python3-setuptools` (only needed on linux, preinstalled with python3 on mac)     
`sudo apt-get install -y pkg-config` (only needed on linux)    
cd into this directory and then run `python3 setup.py install` to install secp256k1.     
After that it should be possible to install the hyperledger sawtooth python sdk (`pip install sawtooth-sdk`, will be run from  requirements.txt)

### More information

To test if local node is running: `curl http://localhost:8008/blocks`
https://sawtooth.hyperledger.org/docs/core/releases/1.0/app_developers_guide/docker.html
   
## Multichain
Build and start the docker container:    
`docker-compose -f docker/docker_multichain/docker-compose.yml up` (on Linux, sudo may be required)    
Look up the name of the running container (column NAMES):    
`sudo docker container ls`    
Enter container:     
`docker exec -it docker_multichain_masternode_1_5454208681af sh`, replace with name of container

Start CLI tool with preconfigured blockchain dockerchain:         
`multichain-cli dockerchain`    

Create keys:        
`>createkeypairs` will return something like this:    
```
[
    {
        "address" : "1LKfR5yQVKx3YJ27enyKDNske7XFHzkN6bm43Y",
        "pubkey" : "0323187cd83c9dde13f223b5df1fb2899e645e8b0cd1fa73ae61c41b07ce9cd7a6",
        "privkey" : "VHrFLuvdBeb1oVTmKD48Sdm1ovoc8mS5pbrk2gpKhCUWh72LavvAF8jx"
    }
]
```
Save the address and privkey in the SQLite DB under `address` resp. `key`.    

Grant the new address send and receive rights:     
`grant [address from beforesend,receive`     
e.g. `grant 1LKfR5yQVKx3YJ27enyKDNske7XFHzkN6bm43Y send,receive`    
Save the resulting transaction hash in de database as transaction (will be used as input).
