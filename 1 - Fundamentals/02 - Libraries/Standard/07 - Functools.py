"""
FUNCTOOLS — Python Standard Library

Provides higher-order functions:
- caching
- partial functions
- reducing
"""

import functools as ft

# ---------------------------------------------------------
# REDUCE
# ---------------------------------------------------------

result = ft.reduce(lambda a, b: a + b, [1, 2, 3, 4])
print(result)

# ---------------------------------------------------------
# PARTIAL FUNCTIONS
# ---------------------------------------------------------

def power(base, exp):
    return base ** exp

square = ft.partial(power, exp=2)
print(square(5))

# ---------------------------------------------------------
# LRU CACHE
# ---------------------------------------------------------

@ft.lru_cache(maxsize=100)
def slow_function(n):
    return n * 2

print(slow_function(10))
