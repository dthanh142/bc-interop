import numpy as np
import matplotlib
import matplotlib as mpl
import matplotlib.pyplot as plt


# Load
EOS_data = np.genfromtxt('/Users/timo/Documents/repos/bc-interop/performance_test/data/EOS.csv', delimiter=',')
EOS_data = EOS_data[~np.isnan(EOS_data)]
POSTGRES_data = np.genfromtxt('/Users/timo/Documents/repos/bc-interop/performance_test/data/POSTGRES.csv', delimiter=',')
POSTGRES_data = POSTGRES_data[~np.isnan(POSTGRES_data)]

print(EOS_data)


def save_to_plot():
	## agg backend is used to create plot as a .png file
	mpl.use('agg')
	## combine these different collections into a list
	data_to_plot = [EOS_data, POSTGRES_data]
	# Create a figure instance
	fig = plt.figure(1, figsize=(9, 6))
	# Create an axes instance
	ax = fig.add_subplot(111)
	# Create the boxplot
	bp = ax.boxplot(data_to_plot)
	# Set labels etc.
	ax.set_xticklabels(['EOS', 'POSTGRES'])
	ax.set_ylabel('Average time for 1000 transactions')
	ax.set_xlabel('Blockchain')
	ax.set_title('Performance Comparison')
	ax.yaxis.grid(True)

	# Save the figure and show
	plt.tight_layout()
	plt.savefig('performance_test/GraphNew.png')


save_to_plot()
