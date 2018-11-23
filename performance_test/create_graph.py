import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt

divider = 1000

BITCOIN_data = np.genfromtxt('performance_test/data/BITCOIN.csv', delimiter=',')
# remove nan values and limit to first 1000 samples and divide by 1000 to get seconds
BITCOIN_data = BITCOIN_data[~np.isnan(BITCOIN_data)][0:1000]/divider
ETHEREUM_data = np.genfromtxt('performance_test/data/ETHEREUM.csv', delimiter=',')
ETHEREUM_data = ETHEREUM_data[~np.isnan(ETHEREUM_data)][0:1000]/divider
MULTICHAIN_data = np.genfromtxt('performance_test/data/MULTICHAIN.csv', delimiter=',')
MULTICHAIN_data = MULTICHAIN_data[~np.isnan(MULTICHAIN_data)][0:1000]/divider
STELLAR_data = np.genfromtxt('performance_test/data/STELLAR.csv', delimiter=',')
STELLAR_data = STELLAR_data[~np.isnan(STELLAR_data)][0:1000]/divider
EOS_data = np.genfromtxt('performance_test/data/EOS.csv', delimiter=',')
EOS_data = EOS_data[~np.isnan(EOS_data)][0:1000]/divider
IOTA_data = np.genfromtxt('performance_test/data/IOTA.csv', delimiter=',')
IOTA_data = IOTA_data[~np.isnan(IOTA_data)][0:1000]/divider
HYPERLEDGER_data = np.genfromtxt('performance_test/data/HYPERLEDGER.csv', delimiter=',')
HYPERLEDGER_data = HYPERLEDGER_data[~np.isnan(
	HYPERLEDGER_data)][0:1000]/divider
POSTGRES_data = np.genfromtxt('performance_test/data/POSTGRES.csv', delimiter=',')
POSTGRES_data = POSTGRES_data[~np.isnan(POSTGRES_data)][0:1000]/divider


def save_to_plot():
	# agg backend is used to create plot as a .png file
	mpl.use('agg')
	# combine these different collections into a list
	data_to_plot = [BITCOIN_data, ETHEREUM_data, MULTICHAIN_data, STELLAR_data, EOS_data, IOTA_data, HYPERLEDGER_data, POSTGRES_data]
	# Create a figure instance
	fig = plt.figure(1, figsize=(9, 6))
	# Create an axes instance
	ax = fig.add_subplot(111)
	# Create the boxplot
	ax.boxplot(data_to_plot)
	# Set labels etc.
	ax.set_xticklabels(['BITCOIN', 'ETHEREUM', 'MULTICHAIN', 'STELLAR', 'EOS', 'IOTA', 'HYPERLEDGER', 'POSTGRES'])
	ax.set_ylabel('Average time per transaction using 1000 samples (in seconds)')
	ax.set_yscale('log')
	ax.set_xlabel('Blockchain')
	ax.set_title('Performance Comparison')
	ax.yaxis.grid(True)
	# Save the figure and show
	plt.tight_layout()
	plt.savefig('performance_test/performance.eps', format='eps')
	# plt.savefig('performance_test/Graph.png')

save_to_plot()
