from blockchain import Blockchain

print(Blockchain["ETHEREUM"].value)

# for bc in Blockchain:
#         connection.execute(
#             '''
#         INSERT INTO blockchains
#         VALUES (?, ?)
#         ''',
#             (bc.value, bc.name)
#         )
