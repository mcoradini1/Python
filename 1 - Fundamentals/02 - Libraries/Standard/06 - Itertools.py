"""
ITERTOOLS — Python Standard Library

Provides tools 5.1 - For efficient looping:
- infinite iterators
- combinations
- permutations
- grouping
"""

import itertools as it

# ---------------------------------------------------------
# COUNT (INFINITE)
# ---------------------------------------------------------

counter = it.count(start=1, step=2)
print(next(counter))
print(next(counter))

# ---------------------------------------------------------
# PERMUTATIONS
# ---------------------------------------------------------

print(list(it.permutations([1, 2, 3], 2)))

# ---------------------------------------------------------
# COMBINATIONS
# ---------------------------------------------------------

print(list(it.combinations([1, 2, 3], 2)))
