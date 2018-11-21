import sys
import os
sys.path.append("/Users/timo/Documents/repos/bc-interop")


from api import store
import string
import random
from blockchain import Blockchain


def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters) for m in range(length))

def run_test(blockchain_name):
	i = 0
	while i < 5:
		store(generate_random_string(10), blockchain_name)
		i += 1


run_test(Blockchain.EOS)
