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

### Install secp256k1
IF there is a certification error installing secp256k1:    
/Applications/Python\ 3.6/Install\ Certificates.command
