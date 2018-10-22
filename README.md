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

### Docker
Stop and remove all container: `docker -f rm $(docker ps -a -q)`

### Usefull python stuff
Print a nice, readable version of a dict:     
```python
import pprint
pprint.pprint(dict)
```