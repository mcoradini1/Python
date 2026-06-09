# ======================================================================================================================
# CHALLENGE 74: Random Tuples: Generate 5 random values and chose the higher and lower.
# ======================================================================================================================

"""
Challenge: 6.1.3 - Random Tuples (074)
Category: 6 - Collections
Concepts Used:
    - import random
    - randint
    - tuples
    - max()
    - min()

Tags: import random, randint, tuples, max(), min()
Status: ✔️ Completed
"""

from random import randint
i = [randint(0,999),randint(0,999),randint(0,999), randint(0,999),randint(0,999)]
print(i)
print(f'The higher value is {max(i)}')
print(f'The lower value is {min(i)}')