"""
RANDOM — Python Standard Library

The random module provides functions 5.1 - For:
- random choices
- random integers
- sampling
- simulating randomness

Useful 5.1 - For:
- simulations
- games
- probability experiments
- Monte Carlo methods
"""

import random
import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# BASIC RANDOM CHOICE
# ---------------------------------------------------------

print(random.choice(['H', 'T']))   # coin flip
print(random.choice(['1', '0']))   # binary choice

# ---------------------------------------------------------
# ROLLING A DIE
# ---------------------------------------------------------

print(random.choice([1, 2, 3, 4, 5, 6]))
print(random.choice(range(1, 7)))

# choose a random die type (6, 8, or 10 sides)
print(random.choice([range(1, 7), range(1, 9), range(1, 11)]))

# ---------------------------------------------------------
# MULTIPLE RANDOM CHOICES
# ---------------------------------------------------------

print("\nRandom rolls:")
for _ in range(10):
    x = random.choice(random.choice([range(1, 7), range(1, 9), range(1, 11)]))
    print(x)

# ---------------------------------------------------------
# HISTOGRAM OF DIE ROLLS (100 rolls)
# ---------------------------------------------------------

rolls = []
for _ in range(100):
    rolls.append(random.choice([1, 2, 3, 4, 5, 6]))

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))
plt.title("100 Die Rolls")
plt.show()

# ---------------------------------------------------------
# HISTOGRAM OF DIE ROLLS (10,000 rolls)
# ---------------------------------------------------------

for _ in range(10000):
    rolls.append(random.choice([1, 2, 3, 4, 5, 6]))

plt.hist(rolls, bins=np.linspace(0.5, 6.5, 7))
plt.title("10,100 Die Rolls")
plt.show()

# ---------------------------------------------------------
# SUM OF 10 DICE (10,000 experiments)
# ---------------------------------------------------------

ys = []
for _ in range(10000):
    total = 0
    for _ in range(10):
        total += random.choice([1, 2, 3, 4, 5, 6])
    ys.append(total)

plt.hist(ys, bins=20)
plt.title("Sum of 10 Dice (10,000 experiments)")
plt.show()

"""
Central Limit Theorem (CLT):
The sum of many independent random variables tends toward a normal distribution,
regardless of the original distribution.

Here:
- each die roll is uniform (flat distribution)
- the sum of 10 dice becomes approximately normal
"""
