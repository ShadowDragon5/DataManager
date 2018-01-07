import Sorting
import Graphs


# Sorting.SortScores(filePath = "score.txt", separator = "\t" * 2, ascending = False, orderBy = 1, ignLines = 4)

# Graphs.LinearAndBar(filePath = "score.txt", exportPath = "Generated.png", ignLines = 4, separator = "\t\t", xFunc = lambda l: int(l[0]), y1Func = lambda l: int(l[1]), y2Func = lambda l: int(l[4]) + int(l[3]))

# Generation / Score / Collectibles
# gen = lambda l: int(l[0])
# score = lambda l: int(l[2])
# coll = lambda l: int(l[4])

# Graphs.LinearAndBar(filePath = "../Data.log", exportPath = "Data.png", ignLines = 2, separator = "\t\t", xFunc = gen, y1Func = score, y2Func = coll, xLabel = "Generation", y1Label = "Score", y2Label = "Collectibles")

data, cont = Sorting.ReadData(filePath = "Data.log", ignLines = 2)
cont = Sorting.ConvertToArray(cont = cont, separator = "\t\t")

Genomes = {}
SS = set()
with open("Trace.log", "r") as fs:
	for x in range(60):
		prefGenes = set()
		gen = 0
		next(fs)
		gen = int(fs.readline()[11:13])
		for i in range(5):
			next(fs)
		for i in range(6):
			line = fs.readline()
			genes = line.split(":")
			genes = list(map(lambda g: g[:-1].strip(), genes[2:]))
			# print(genes)
			if (line[14:15] == "F"):
				prefGenes.add(genes[0])
			else:
				prefGenes.add(genes[1])
		next(fs)

		if (frozenset(prefGenes) not in Genomes):
			Genomes[frozenset(prefGenes)] = [gen]
			SS.add(frozenset(prefGenes))
		else:
			Genomes[frozenset(prefGenes)].append(gen)
# print(Genomes)
Graphs.ErrorBar(Genomes, list(map(lambda l: int(l[2]), cont)))


print("Job's Done!")