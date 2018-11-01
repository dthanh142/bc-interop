# Blockchain Interoperability

## Setup
### Using venv
Create environment:
`python3 -m venv venv`    
Activate environment:
`source venv/bin/activate`
The python version of the environment will be the one with which the environment is created.
  
### Export dependencies
`venv/bin/pip freeze > requirements.txt`

### Import dependencies
`venv/bin/pip install -r requirements.txt`

### Create and source database
Create local DB: `import db.database`
Source database: `db.database.setup()`

### Upgrade pip on <3.6
Use this command if upgrading pip fails due to SSL cert error:    
`curl https://bootstrap.pypa.io/get-pip.py | python`

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


### Docker
Stop and remove all container: `docker rm -f $(docker ps -a -q)`

### Usefull python stuff
Print a nice, readable version of a dict:     
```python
import pprint
pprint.pprint(dict)
```

Print object keys: 
print(dir(obj))