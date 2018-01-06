'''Score Calculation for ESJMK Project'''
import random as ran
import Sorting
import math


def FillWeights(w):
	"""Fills list w/ weights"""
	w[0] = 5		# 14			# Collectible
	w[4] = w[0] / 2.0				# Collectibles in inventory
	w[1] = 2		# 3.59			# Time
	w[2] = 1		# .53			# Fire time
	w[3] = 1.5		# 1.55			# Fire time w/ collectibles


def GenValues(givenTime, maxColl):
	"""Generates random values"""
	time = int(givenTime - (ran.randrange(givenTime) + 60))		#Time left

	if time <= 0:
		collCount = int(ran.randrange(maxColl))
		curColl = int(ran.randrange(3 if (maxColl - collCount >= 2) else 2 if (maxColl - collCount == 1) else 0))
		time = 0
	else:
		collCount = int(maxColl)
		curColl = 0

	fireTime = float(ran.uniform(0, 50))	# givenTime - time
	fireCollTime = float(ran.uniform(0, fireTime))

	if round(fireTime) != 0:
		fireCount = int(ran.randrange(round(fireTime)) + 1)
	elif round(fireTime * 100) != 0:
		fireCount = int(ran.randrange(round(fireTime * 100)) + 1)
	else:
		fireCount = 0

	return time, collCount, curColl, fireTime, fireCollTime, fireCount


def Score(w, time, collCount, curColl, fireTime, fireCollTime, fireCount):
	"""Calculates Score (0 <= score =< 1000)"""

	# \/ OLD
	# return + collCount * w[0] + (time * w[1]) - (fireTime * w[2] + fireCollTime * w[3]) * (fireCount / 100 + 1) + 499.2

	# NEW
	score = 0

	# Good
	score += + (collCount) ** 2 * w[0]	# More collectibles collected
	score += + (curColl) ** 2 * w[4]
	score += + (time) * w[1] 				# More time left

	# Bad
	mul = fireCount / 100 + 1
	score += - ((fireTime - fireCollTime) * w[2]) * mul		# More times entered the worse
	score += - fireCollTime * w[3] * mul		# 

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
	out.write("MIN: {min:.2f}\n".format(min = Score(W, time = 0, collCount = 0, curColl = 0, fireTime = 115, fireCollTime = 110, fireCount = 100)))
	out.write("MAX: {max:.2f}\n".format(max = Score(W, time = 120, collCount = MaxColl, curColl = 0, fireTime = 0, fireCollTime = 0, fireCount = 0)))
	out.write("NONE: {non:.2f}\n".format(non = Score(W, time = 0, collCount = 0, curColl = 0, fireTime = 0, fireCollTime = 0, fireCount = 0)))

	# Titles of the columns
	out.write("Gen\t\tScore\t\tTime\t\tColl\t\t\tFire Times\n")

	# Generates 50 results
	for x in range(50):
		Time, CollCount, CurColl, FireTime, FireCollTime, FireCount = GenValues(GivenTime, MaxColl)

		score = Score(W, Time, CollCount, CurColl, FireTime, FireCollTime, FireCount)

		if score < 0:
			print("Negative")

		out.write("{:2}\t\t{:4.0f}\t\t{:2}\t\t{}\t\t{}\t\t{:6.2f}\t\t{:5.2f}\t\t{:3}\n".format(x, score, Time, CollCount, CurColl, FireTime,FireCollTime, FireCount))

# Sorts data
# Sorting.SortScores(filePath = File, ascending = True, orderBy = 1, ignLines = 4)


print("Job's Done!")