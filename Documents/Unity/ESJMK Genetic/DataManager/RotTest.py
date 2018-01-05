'''Smooth rotation test'''
import math as m
# from collections import namedtuple

class Vec3:
	"""Vector of x y z"""
	def __init__(self, x = 0.0, y = 0.0, z = 0.0):
		super().__init__()
		self.x = x
		self.y = y
		self.z = z

	def __str__(self):
		return "( {x:.3f} ; {y:.3f} ; {z:.3f} )".format(x = self.x, y = self.y, z = self.z)


# MAIN ---------------------------------------------------
if (__name__ == "__main__"):
	print(__doc__)

"""
z - backwards
x - across
	-
  +   -
	+
rotates counter clockwise
"""

start = Vec3(1, 0, -1)
curr = start
step = m.radians(360 / 4)
cAngle = 0.0

angle = m.radians(90)

if (angle < 0):
	step = -step
	angle = abs(angle)

while (abs(cAngle) < angle):

	x = m.cos(step) * curr.x - m.sin(step) * curr.z
	z = m.sin(step) * curr.x + m.cos(step) * curr.z

	curr = Vec3(x, 0, z)
	# print(curr)
	cAngle += step

	
print(start)
print(curr)
print("Rotated by {:.3f} degrees (goal: {:.3f}).".format(m.degrees(cAngle), m.degrees(angle)))
