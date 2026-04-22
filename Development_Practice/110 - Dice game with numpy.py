#Using Numpy prepare a die game.

import numpy as np
import matplotlib.pyplot as plt
#AM SUMMING THE COLUMNS HERE, SO EACH
x1 = np.random.randint(1,7, (1000000,10))
y1 = np.sum(x1, axis=1)

plt.hist(y1)
print(y1)
print(max(y1))
print(min(y1))
plt.show()

