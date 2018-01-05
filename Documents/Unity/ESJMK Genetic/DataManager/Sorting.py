"""Collection functions for sorting data"""
import Errors

if (__name__ == "__main__"):
	print(__doc__)


def Descending(ls, e):
	"""Sorts list of lists in descending order by element"""
	for i in range(len(ls) - 1):

		for j in range(i + 1, len(ls)):

			if float(ls[i][e]) < float(ls[j][e]):

				ls[i], ls[j] = ls[j], ls[i]		#swap
	return ls


def ReadData(filePath, ignLines):
	data = []

	# Gets data from file
	try:
		with open(filePath, "r") as fs:
			# Ignoring lines at the start of file
			for x in range(ignLines):
				data.append(fs.readline())

			cont = fs.readlines()
			
	except Exception as e:
		Errors.ErrorMessage("Failed to read data from file!", e)
	
	return data, cont





def SortScores(filePath, separator = "\t\t", ascending = False, orderBy = 1, ignLines = 1):
	""" """
	data, cont = ReadData(filePath, ignLines)

	# Prep data for sorting
	cont = [line.split(separator) for line in cont]
	
	# Sort data
	if ascending:
		data += Descending(ls = cont, e = orderBy)[::-1]
	else:
		data += Descending(ls = cont, e = orderBy)

	# Writes sorted data back to file
	with open(filePath, "w") as fv:
		for x in range(ignLines):
			fv.write("{}".format(data[x]))
			
		for line in data[ignLines:]:
			fv.write(separator.join(line))