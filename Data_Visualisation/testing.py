import matplotlib.pyplot as plt

values = [10, 13, 11, 15, 20]
yerr = [1, 3, 0.5, 2, 4]
plt.bar(range(len(values)), values, yerr=yerr, capsize=10)
plt.show()
