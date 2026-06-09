"""
NUMPY RANDOM — Third-Party Library

NumPy's random module provides:
- random floats
- normal distributions
- random integers
- random matrices
- sampling utilities
"""

import numpy as np

# ---------------------------------------------------------
# RANDOM FLOATS
# ---------------------------------------------------------

np.random.random(5)          # 1D array
np.random.random((5, 5))     # 2D array

# ---------------------------------------------------------
# NORMAL DISTRIBUTION
# ---------------------------------------------------------

# np.random.normal(mean, std, size)
np.random.normal(0, 1, 5)
np.random.normal(0, 1, (2, 5))

# ---------------------------------------------------------
# RANDOM INTEGERS
# ---------------------------------------------------------

x = np.random.randint(1, 7, (10, 3))
print(x)
print(x.shape)

# ---------------------------------------------------------
# SUM ACROSS AXES
# ---------------------------------------------------------

print(np.sum(x))             # total sum
print(np.sum(x, axis=0))     # sum of rows
print(np.sum(x, axis=1))     # sum of columns
