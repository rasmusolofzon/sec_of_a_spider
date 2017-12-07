import random
import hashlib
import matplotlib

k = random.getrandbits(16)
v = random.getrandbits(1)

for X in range(1,17):
    ...
    #binding
    #concealing

print("k = {0}, type {1}".format(k, type(k)))

# import matplotlib.path as mpath
# import matplotlib.patches as mpatches
# import matplotlib.pyplot as plt

# Path = mpath.Path

# fig, ax = plt.subplots()
# pp1 = mpatches.PathPatch(
#     Path([(0, 0), (1, 0), (1, 1), (0, 0)],
#          [Path.MOVETO, Path.CURVE3, Path.CURVE3, Path.CLOSEPOLY]),
#     fc="none", transform=ax.transData)

# ax.add_patch(pp1)
# ax.plot([0.75], [0.25], "ro")


import matplotlib.pyplot as plt
import matlotlib.mlab as mlab
import numpy as np

fig, ax = plt.subplots()
probabilities = np.arange(0, 1, 0.1)
index = np.arange(len(probabilities))
print(index)
print(probabilities)

fig.suptitle("HA3 - B1")

handlebar = ax.bar(index, probabilities, label="Simulated probabilities")

ax.set_xlabel("X (length of cut-off)")
ax.set_ylabel("Probability of breaking property")
ax.set_xticks(index)

plt.show()


##################################
# Data structures after completion
##################################
# binding 
# {1: 0.9, 2: 0.8, 3: 0.7, ...}

# concealing data structure
# {1: (True, 1234), 2: (False, 1235), ...}

