'''Score Calculation for ESJMK Project'''
import random as ran
import Sorting
import math


def FillWeights(w):
	"""Fills list w/ weights"""
	w[0] = 14		# 14			# Collectible
	w[1] = 3.5		# 3.59			# Time
	w[2] = .5		# .53			# Fire time
	w[3] = 1.5		# 1.55			# Fire time w/ collectibles


def GenValues(givenTime, maxColl):
	"""Generates random values"""
	time = int(givenTime - (ran.randrange(givenTime) + 30))		#Time left

	if time <= 0:
		collCount = int(ran.randrange(maxColl - 1))
		time = 0
	else:
		collCount = int(maxColl)

	fireTime = float(ran.uniform(0, givenTime - time))
	fireCollTime = float(ran.uniform(0, fireTime))

	if round(fireTime) != 0:
		fireCount = int(ran.randrange(round(fireTime)) + 1)
	elif round(fireTime * 100) != 0:
		fireCount = int(ran.randrange(round(fireTime * 100)) + 1)
	else:
		fireCount = 0

	return time, collCount, fireTime, fireCollTime, fireCount


def Score(w, time, collCount, fireTime, fireCollTime, fireCount):
	"""Calculates Score (0 <= score =< 1000)"""

	# \/ OLD
	# return + collCount * w[0] + (time * w[1]) - (fireTime * w[2] + fireCollTime * w[3]) * (fireCount / 100 + 1) + 499.2

	# NEW
	score = 0

	func = lambda x: 2 ** x
	# func = math.exp

	# Good
	score += + func(collCount) # * w[0]								# More collectibles collected
	score += + time * w[1] 								# More time left

	func = lambda x: x 

	# Bad
	score += - ((fireTime - fireCollTime) * w[2]) * (func(fireCount) / 100 + 1) 		# More times entered the worse
	score += - fireCollTime * w[3] * (func(fireCount) / 100 + 1)		# 

	return score



# MAIN-------------------------------------------------------------
if (__name__ == "__main__"):
	print(__doc__)

File = "score.txt"
FireCount = int(0)
CurrentScore = int(0)

GivenTime = int(120)
MaxColl = int(5)

# Weight list
W = [1] * 10
FillWeights(W)

with open(File, "w") as out:

	# Possible values
	out.write("MIN: {min:.2f}\n".format(min = Score(W, time = 0, collCount = 0, fireTime = 115, fireCollTime = 110, fireCount = 100)))
	out.write("MAX: {max:.2f}\n".format(max = Score(W, time = 120, collCount = MaxColl, fireTime = 0, fireCollTime = 0, fireCount = 0)))
	out.write("NONE: {non:.2f}\n".format(non = Score(W, time = 0, collCount = 0, fireTime = 0, fireCollTime = 0, fireCount = 0)))

	# Titles of the columns
	out.write("Gen\t\tScore\tTime\tColl\t\tFire Times\n")

	# Generates 50 results
	for x in range(50):
		Time, CollCount, FireTime, FireCollTime, FireCount = GenValues(GivenTime, MaxColl)

		score = Score(W, Time, CollCount, FireTime, FireCollTime, FireCount)

		if score < 0:
			print("Negative")

		out.write("{:2}\t\t{:4.0f}\t\t{:2}\t\t{}\t\t{:6.2f}\t\t{:5.2f}\t\t{:3}\n".format(x, score, Time, CollCount, FireTime,FireCollTime, FireCount))

# Sorts data
# Sorting.SortScores(filePath = File, ascending = True, orderBy = 1, ignLines = 4)


print("Job's Done!")