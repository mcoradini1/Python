import time
import random

start = time.time()

ys = []
x = []
for rep in range (100):
    y = 0
    for k in range (10):
        x = random.choice([1, 2, 3, 4, 5, 6])
        y = y + x
    ys.append(y)

print(len(ys),max(ys),min(ys))


end = time.time()

final = end - start
print(final)




