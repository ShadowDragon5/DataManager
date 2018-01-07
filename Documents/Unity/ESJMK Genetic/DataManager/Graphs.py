import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

import Sorting

# "score.txt", "Data.png", 4, "\t\t", gen = list(map(lambda l: int(l[0]), cont)), score = list(map(lambda l: int(l[1]), cont)), coll = list(map(lambda l: int(l[4]) + int(l[3]), cont)), 
def LinearAndBar(filePath, exportPath, ignLines, separator, xFunc, y1Func, y2Func, xLabel = "X", y1Label = "Y1", y2Label = "Y2", color1 = "blue", color2 = "red"):
	"""Graphs linear and bar graphs on the same image"""
	data, cont = Sorting.ReadData(filePath = filePath, ignLines = ignLines)
	cont = Sorting.ConvertToArray(cont = cont, separator = separator)
	cont = Sorting.Descending(ls = cont, e = 4)

	x = list(map(xFunc, cont))
	y1 = list(map(y1Func, cont))
	y2 = list(map(y2Func, cont))

	ind = np.arange(len(x) / 2)
	width = .4

	x[1::2] = map(lambda l: l + width, x[1::2])
	# First graph
	fig, ax1 = plt.subplots()
	ax1.axhline(y=0, color='k', alpha = .75)
	# ax1.axvline(x=0, color='k')
	plt.xlabel(xLabel)
	ax1.plot(x, y1, color = color1, linewidth = 2, alpha = 1)
	ax1.set_ylabel(y1Label, color = color1)
	ax1.tick_params("y", colors = color1)
	ax1.grid(True, color = color1, alpha = 0.5)
	# ax1.set_xticklabels(list(map(lambda l: int(l[0]), cont)))

	# Second graph
	ax2 = ax1.twinx()
	ax2.bar(x, y2, width = width, color = color2, alpha = .6, edgecolor = "#4d0000")
	ax2.set_ylabel(y2Label, color = color2)
	ax2.tick_params("y", colors = color2)
	ax2.grid(True, color = color2, alpha = 0.5)

	# Second graph
	# ax2.bar(list(map(lambda i: i + width, x[1::2])), y2[1::2], width = width, color = color2, alpha = .6)

	ax1.xaxis.set_major_locator(ticker.MaxNLocator(integer=True))
	ax1.yaxis.set_major_locator(ticker.MaxNLocator(integer=False))
	ax2.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))


	fig.tight_layout()
	plt.savefig(exportPath)
#----------------------


def ErrorBar(dic, score):
	for k, v in dic.items():
		dic[k] = [score[i] for i in v]

	x = list(map(lambda k: ", ".join(k), dic.keys()))
	y = list(map(lambda v: sum(v) / len(v), dic.values()))
	mxy = list(map(lambda v: - max(v) + sum(v) / len(v), dic.values()))
	mny = list(map(lambda v: - sum(v) / len(v) + min(v), dic.values()))

	fig, ax = plt.subplots()
	ax.errorbar(x, y, yerr = [mxy, mny], fmt = 'dk', capsize = 5, ecolor = "blue");
	# ax.plot(x, y, "--k")
	ax.set_ylabel("Score")
	ax.axhline(y=0, color='k', alpha = .75)
	ax.grid(True, alpha = 0.5)

	fig.autofmt_xdate()
	fig.tight_layout()
	plt.savefig("Generations.png")





# plt.bar(x, y, color = "#FF1C1CFF")