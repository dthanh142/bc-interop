# Blockchain Interoperability

## Usage

```python
from api import store, retrieve, migrate, Blockchain

tx_hash = store('Some Data', Blockchain.STELLAR)    

data = retrieve('[Transaction_Hash]')    

tx_hash = migrate('[Transaction_Hash]', Blockchain.ETHEREUM)
```


## Setup

### Python Setup
Linux: https://askubuntu.com/questions/682869/how-do-i-install-a-different-python-version-using-apt-get

### Python Setup

#### Linux
Install docker from https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1 and `sudo apt-install docker-compose`

#### Mac
https://docs.docker.com/docker-for-mac/install/ (compose will be installed)


#### How to use venv
(On linux)
`sudo apt-get install python3-venv`
Create environment:
`python3 -m venv venv` (on mac)
`python3.5 -m venv --without-pip venv` and `curl https://bootstrap.pypa.io/get-pip.py | python` (on linux, venv is broken on 3.5 for ubuntu)
Activate environment:
`source venv/bin/activate`
The python version of the environment will be the one with which the environment is created.
Deactivate environment:
`(venv) $ deactivate`
  
#### Export and import dependencies
`venv/bin/pip freeze > requirements.txt`
`pip freeze > requirements.txt` (linux)
`venv/bin/pip install -r requirements.txt`
Installing the requirements will most likely fail due to sawtooth-sdk incompatibility issues with python 3.6.      
Look at the Sawtooth section of setup.md to fix this.

#### Upgrade pip on <3.6
Use this command if upgrading pip fails due to SSL cert error:    
`curl https://bootstrap.pypa.io/get-pip.py | python`

### Database Setup
Install sqlite:    
`pip install sqlite`

Run the database setup:

```python
import db.database
db.database.setup()
```

> Calling the `setup` function of the [`database`](database.py) module will:
>
> 1. drop `credentials` and `transactions` tables if they already exist
> 2. create tables for storing `credentials` and `transactions`
> 3. seed the `credentials` table with credentials for Ethereum, MultiChain and Bitcoin
> 4. seed the `transactions` table with input transactions for MultiChain and Bitcoin

> Seed values are read from the [`config`](config.py) module.

### Blockchain Setup
See descriptions in SETUP.md



### Misc 
#### Stop and remove all docker container: 
`docker rm -f $(docker ps -a -q)`
##### Delete all images
`docker rmi $(docker images -q)`


#### Print a nice, readable version of a dict:     
```python
import pprint
pprint.pprint(dict)
```

#### Print object keys: 
print(dir(obj))
