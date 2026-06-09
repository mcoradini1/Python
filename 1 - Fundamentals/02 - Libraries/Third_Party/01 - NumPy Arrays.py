"""
NUMPY — Third-Party Library

NumPy is a fundamental package 5.1 - For scientific computing in Python.
It provides:
- n-dimensional array objects
- fast vectorized operations
- mathematical functions
- broadcasting
- integration with C/C++/Fortran

More info: https://numpy.org
"""

import numpy as np

# ---------------------------------------------------------
# ZERO ARRAYS
# ---------------------------------------------------------

zero_vector = np.zeros(5)          # 1D array of zeros
zero_matrix = np.zeros((5, 3))     # 2D array (5 rows, 3 columns)

print(zero_vector)
print(zero_matrix)

# ---------------------------------------------------------
# BASIC ARRAYS (1D)
# ---------------------------------------------------------

x = np.array([1, 2, 3])
y = np.array([2, 4, 6])

print(x)
print(y)

print(x.shape)   # shape attribute
print(x.size)    # size attribute

# ---------------------------------------------------------
# BASIC ARRAYS (2D)
# ---------------------------------------------------------

z = np.array([[1, 3],
              [5, 9]])

print(z)

# ---------------------------------------------------------
# TRANSPOSE
# ---------------------------------------------------------

print(z.transpose())

# ---------------------------------------------------------
# SLICING (1D)
# ---------------------------------------------------------

print(x[0])
print(x[0:2])
print(x + y)

# ---------------------------------------------------------
# SLICING (2D) — COLUMNS
# ---------------------------------------------------------

x2 = np.array([[1, 2, 3],
               [4, 5, 6]])

y2 = np.array([[2, 4, 6],
               [8, 10, 12]])

print(x2[:, 1])          # column 1
print(y2[:, 1])
print(x2[:, 1] + y2[:, 1])

# ---------------------------------------------------------
# SLICING (2D) — ROWS
# ---------------------------------------------------------

print(x2[1, :])
print(y2[1, :])
print(x2[1, :] + y2[1, :])

# ---------------------------------------------------------
# INDEXING WITH LISTS / ARRAYS
# ---------------------------------------------------------

index_array = np.array([0, 2, 3])
index_list = [0, 2, 3]

z1 = np.array([1, 3, 5, 7, 9])
z2 = z1 + 1

print(z1[index_array])
print(z1[index_list])

# Boolean indexing
print(z1 > 6)
print(z1[z1 > 6])

mask = z1 > 6
z4 = np.array([8, 16, 32, 33, 0])

print(z1[mask])
print(z2[mask])
print(z4[mask])

# ---------------------------------------------------------
# COPYING ARRAYS
# ---------------------------------------------------------

# INCORRECT (creates a view)
w = z1[0:3]
w[0] = 8
print(z1)

# CORRECT (creates a copy)
indices = [0, 1, 2]
w = z1[indices]
w[0] = 43
print(z1)

# ---------------------------------------------------------
# LINSPACE / LOGSPACE
# ---------------------------------------------------------

np.linspace(0, 100, 10)
np.logspace(1, 2, 10)
print(np.logspace(np.log10(250), np.log10(500), 10))

# ---------------------------------------------------------
# RANDOM ARRAYS (BASIC)
# ---------------------------------------------------------

random_np = np.random.random(10)
print(random_np)
print(np.any(random_np > 0.9))
print(np.all(random_np >= 0.1))
