import random
import matplotlib.pyplot as plt
import numpy as np

#The probability of each number is the same, that brings the theory that the histogram tends to be FLAT,
# as we increase the number of visualizations. to check that see it bellow.

#THROW  DIE 100 TIMES --------------------------------------------------------------------------------------------------
rolls = []
for k in range (100):
    x = random.choice([1, 2, 3, 4, 5, 6])
    rolls.append(x)
print(len(rolls))
print(rolls)

plt.hist(rolls, bins = np.linspace(0.5,6.5,7))
plt.show()

#THROW  DIE 10000 TIMES ------------------------------------------------------------------------------------------------
for k in range (10000):
    x = random.choice([1, 2, 3, 4, 5, 6])
    rolls.append(x)
print(len(rolls))
print(rolls)

plt.hist(rolls, bins = np.linspace(0.5,6.5,7))
plt.show()

#THROW 10 DIE 10000 TIMES ----------------------------------------------------------------------------------------------

ys = []
x = []
for rep in range (10000):
    y = 0
    for k in range (10):
        x = random.choice([1, 2, 3, 4, 5, 6])
        y = y + x
    ys.append(y)

print(len(ys),max(ys),min(ys))
plt.hist(ys)
plt.show()

#Central Limit Theorem (CLT) says about the sum or larger numbers of random variables, regardless of their
# distribution it will be proximate to a normal distribution.