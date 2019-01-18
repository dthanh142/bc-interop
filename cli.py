from PyInquirer import prompt, print_json, style_from_dict, Token, Separator

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
					'name': 'Bitcoin'
				},
				{
					'name': 'Ethereum'
				},
				{
					'name': 'Stellar'
				},
				{
					'name': 'EOS'
				},
				{
					'name': 'IOTA'
				},
				{
					'name': 'Hyperledger'
				},
				{
					'name': 'Multichain'
				},
				{
					'name': 'Postgres'
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
	print(f"{answer} and method was store")

if(action == 'Retrieve'):
	questions = [
		{
			'type': 'input',
			'name': 'hash',
			'message': 'Please input the transaction hash',
		}
	]
	answer = prompt(questions)
	print(f"{answer} and method was retrieve")

if(action == 'Retrieve'):
	questions = [
		{
			'type': 'list',
			'message': 'Select action',
			'name': 'blockchain',
			'choices': [
				{
					'name': 'Bitcoin'
				},
				{
					'name': 'Ethereum'
				},
				{
					'name': 'Stellar'
				},
				{
					'name': 'EOS'
				},
				{
					'name': 'IOTA'
				},
				{
					'name': 'Hyperledger'
				},
				{
					'name': 'Multichain'
				},
				{
					'name': 'Postgres'
				},
			],
		},
		{
			'type': 'input',
			'name': 'hash',
			'message': 'Please input the transaction hash',
		}
	]
	answer = prompt(questions)
	print(f"{answer} and method was migrate")


else:
	print(f"This was a strange input: {action}... please try again")

# answers = prompt(questions)


# print(answers)


# print(store("timoishere", Blockchain.STELLAR))


# print(
#     retrieve(
#         "e229c47f66d3ed3b9076e86a37862738a2e5770009654e8a3cc75458924851da"
#     ))
# print(migrate("f12cc0275e47d8040c04d0ea0d26bf8117f25e0628697da338f73e1eb3d39cad;25316099",
#         Blockchain.STELLAR))
