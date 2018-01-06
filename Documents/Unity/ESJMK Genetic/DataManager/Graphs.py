import matplotlib.pyplot as plt
import numpy as np

import Sorting

data, cont = Sorting.ReadData("score.txt", 4)
cont = Sorting.ConvertToArray(cont, "\t\t")


gen = list(map(lambda l: int(l[0]), cont))
score = list(map(lambda l: int(l[1]), cont))
coll = list(map(lambda l: int(l[4]) + int(l[3]), cont))

color1 = "blue"
fig, ax1 = plt.subplots()
ax1.plot(gen, score, color = color1, linewidth = 2, alpha = 1, zorder = 2)
ax1.set_ylabel("Score", color = color1)
ax1.tick_params("y", colors = color1)

plt.xlabel("Generation")

color2 = "#FF1C1CFF"
ax2 = ax1.twinx()
ax2.bar(gen, coll, color = color2, alpha = .5, zorder = 1)
ax2.set_ylabel("Collectibles", color = color2)
ax2.tick_params("y", colors = color2)

# plt.errorbar(x, y, yerr = 25, fmt = 'dk', capsize = 2);
# plt.bar(x, y, color = "#FF1C1CFF")


plt.grid(True)
plt.savefig("Data.png")
#----------------------

# fig, ax1 = plt.subplots()


# ax1.plot(t, s1, 'b-')
# ax1.set_xlabel('time (s)')

# ax1.set_ylabel('exp', color='b')
# ax1.tick_params('y', colors='b')

# ax2 = ax1.twinx()
# s2 = np.sin(2 * np.pi * t)
# ax2.plot(t, s2, 'r.')
# ax2.set_ylabel('sin', color='r')
# ax2.tick_params('y', colors='r')

# fig.tight_layout()