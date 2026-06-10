# ======================================================================================================================
# CHALLENGE 110: Numpy six-side die: Roll the die x times
# ======================================================================================================================

"""
Challenge: 9.1 - Numpy six-side die (110)
Category: 9 - Modules and Imports
Concepts Used:


Tags: import numpy, matplotlib, plt.hist, plt.show, min(), max()
Status: ✔️ Completed
"""
#Using Numpy prepare a die game.

import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.randint(1,7, (1000000,10))
y1 = np.sum(x1, axis=1)

plt.hist(y1)
print(y1)
print(max(y1))
print(min(y1))
plt.show()

