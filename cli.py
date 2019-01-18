# append the root project path to the pythonpath so that blockchain.py can be accessed by every adapter
import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")
from PyInquirer import prompt, print_json, style_from_dict, Token, Separator
from blockchain import Blockchain
import api

questions = [
	{
		'type': 'list',
		'message': 'Select action',
		'name': 'actions',
		'choices': [
			{
				'name': 'Store'
			},
			{
				'name': 'Retrieve'
			},
			{
				'name': 'Migrate'
			},
		],
	},

]
action = prompt(questions)['actions']


if(action == 'Store'):
	questions = [
		{
			'type': 'list',
			'message': 'Select action',
			'name': 'blockchain',
			'choices': [
				{
					'name': 'Bitcoin',
					'value': Blockchain.BITCOIN,
				},
				{
					'name': 'Ethereum',
					'value': Blockchain.ETHEREUM,
				},
				{
					'name': 'Stellar',
					'value': Blockchain.STELLAR,
				},
				{
					'name': 'EOS',
					'value': Blockchain.EOS,
				},
				{
					'name': 'IOTA',
					'value': Blockchain.IOTA,
				},
				{
					'name': 'Hyperledger',
					'value': Blockchain.HYPERLEDGER,
				},
				{
					'name': 'Multichain',
					'value': Blockchain.MULTICHAIN,
				},
				{
					'name': 'Postgres',
					'value': Blockchain.POSTGRES,
				},
			],
		},
		{
			'type': 'input',
			'name': 'data',
			'message': 'Please input the data to store',
		}
	]
	answer = prompt(questions)
	api.store(answer['data'], answer['blockchain'])

elif(action == 'Retrieve'):
	questions = [
		{
			'type': 'input',
			'name': 'hash',
			'message': 'Please input the transaction hash',
		}
	]
	answer = prompt(questions)
	api.retrieve(answer['hash'])

elif(action == 'Migrate'):
	questions = [
		{
			'type': 'input',
			'name': 'hash',
			'message': 'Please input the hash of the transaction connected to the data',
		},
		{
			'type': 'list',
			'name': 'blockchain',
			'message': 'Please select which Blockchain to migrate to',
			'choices': [
				{
					'name': 'Bitcoin',
					'value': Blockchain.BITCOIN,
				},
				{
					'name': 'Ethereum',
					'value': Blockchain.ETHEREUM,
				},
				{
					'name': 'Stellar',
					'value': Blockchain.STELLAR,
				},
				{
					'name': 'EOS',
					'value': Blockchain.EOS,
				},
				{
					'name': 'IOTA',
					'value': Blockchain.IOTA,
				},
				{
					'name': 'Hyperledger',
					'value': Blockchain.HYPERLEDGER,
				},
				{
					'name': 'Multichain',
					'value': Blockchain.MULTICHAIN,
				},
				{
					'name': 'Postgres',
					'value': Blockchain.POSTGRES,
				},
			],
		},
	]
	answer = prompt(questions)
	api.migrate(answer['hash'], answer['blockchain'])

else:
	print(f"This was a strange input: {action}... please try again")
