# append the root project path to the pythonpath so that blockchain.py can be accessed by every adapter
import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from blockchain import Blockchain
import api



questions = [
    {
    		'type': 'input',
    		'message': 'how old are you?',
    		'name': 'action',
    		'validate': lambda output: True if (output=="a") else False
    },

    ]
answer = prompt(questions)['action']


# questions = [
# 	{
# 		'type': 'list',
# 		'message': 'Select action',
# 		'name': 'action',
# 		'choices': [
# 			{
# 				'name': 'Store'
# 			},
# 			{
# 				'name': 'Retrieve'
# 			},
# 			{
# 				'name': 'Migrate'
# 			},
# 		],
# 		'validate': lambda action: 'You must choose at least one topping.'
#             if not action else True
# 	},

# ]
# answer = prompt(questions)['action']


# if(answer == 'Store'):
# 	questions = [
# 		{
# 			'type': 'list',
# 			'message': 'Select action',
# 			'name': 'blockchain',
# 			'choices': [
# 				{
# 					'name': 'Bitcoin',
# 					'value': Blockchain.BITCOIN,
# 				},
# 				{
# 					'name': 'Ethereum',
# 					'value': Blockchain.ETHEREUM,
# 				},
# 				{
# 					'name': 'Stellar',
# 					'value': Blockchain.STELLAR,
# 				},
# 				{
# 					'name': 'EOS',
# 					'value': Blockchain.EOS,
# 				},
# 				{
# 					'name': 'IOTA',
# 					'value': Blockchain.IOTA,
# 				},
# 				{
# 					'name': 'Hyperledger',
# 					'value': Blockchain.HYPERLEDGER,
# 				},
# 				{
# 					'name': 'Multichain',
# 					'value': Blockchain.MULTICHAIN,
# 				},
# 				{
# 					'name': 'Postgres',
# 					'value': Blockchain.POSTGRES,
# 				},
# 			],
# 			'validate': lambda answer: 'You must choose at least one topping.'
#                     if not answer['blockchain'] else True
# 		},
# 		{
# 			'type': 'input',
# 			'name': 'data',
# 			'message': 'Please input the data to store',
# 			'validate': lambda answer: 'You must choose at least one topping.'
#                     if not answer['data'] else True
# 		}
# 	]
# 	answer = prompt(questions)
# 	api.store(answer['data'], answer['blockchain'])

# elif(answer == 'Retrieve'):
# 	questions = [
# 		{
# 			'type': 'input',
# 			'name': 'hash',
# 			'message': 'Please input the transaction hash',
# 		}
# 	]
# 	answer = prompt(questions)
# 	api.retrieve(answer['hash'])

# elif(answer == 'Migrate'):
# 	questions = [
# 		{
# 			'type': 'input',
# 			'name': 'hash',
# 			'message': 'Please input the hash of the transaction connected to the data',
# 		},
# 		{
# 			'type': 'list',
# 			'name': 'blockchain',
# 			'message': 'Please select which Blockchain to migrate to',
# 			'choices': [
# 				{
# 					'name': 'Bitcoin',
# 					'value': Blockchain.BITCOIN,
# 				},
# 				{
# 					'name': 'Ethereum',
# 					'value': Blockchain.ETHEREUM,
# 				},
# 				{
# 					'name': 'Stellar',
# 					'value': Blockchain.STELLAR,
# 				},
# 				{
# 					'name': 'EOS',
# 					'value': Blockchain.EOS,
# 				},
# 				{
# 					'name': 'IOTA',
# 					'value': Blockchain.IOTA,
# 				},
# 				{
# 					'name': 'Hyperledger',
# 					'value': Blockchain.HYPERLEDGER,
# 				},
# 				{
# 					'name': 'Multichain',
# 					'value': Blockchain.MULTICHAIN,
# 				},
# 				{
# 					'name': 'Postgres',
# 					'value': Blockchain.POSTGRES,
# 				},
# 			],
# 		},
# 	]
# 	answer = prompt(questions)
# 	api.migrate(answer['hash'], answer['blockchain'])

# else:
# 	print(f"This was a strange input: {answer}... please try again")
