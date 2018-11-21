# Blockchain Interoperability

## Setup

### Python Setup

#### How to use venv
Create environment:
`python3 -m venv venv`    
Activate environment:
`source venv/bin/activate`
The python version of the environment will be the one with which the environment is created.
Deactivate environment:
`(venv) $ deactivate`
  
#### Export and import dependencies
`venv/bin/pip freeze > requirements.txt`
`venv/bin/pip install -r requirements.txt`

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