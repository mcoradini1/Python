'''
random walk simple
start from (0,0)
place 1 (8,3) time 1
place (7,6) time 2
'''

import matplotlib.pyplot as plt
import numpy as np

delta_x = np.random.normal(0,1,(2,5))
print(delta_x)
plt.plot(delta_x[0], delta_x[1], 'go')
plt.show()
print('fixing a bit more...')

#this is almost done, i just neeed the cumulative section
#exaple (2,4,1,3,2) -> 2,6,7,10,12
#cumulative sum cumsum
#numpy.cumsum(

x_sums = np.cumsum(delta_x,axis=1)
plt.plot(x_sums[0], x_sums[1], 'go-')
plt.show()
print('now starting from 0')

#concatenating numpy.concatenate
x_0 = np.array([[0],[0]])

x_final = np.concatenate((x_0,x_sums), axis=1)
print(x_final)
plt.plot(x_final[0], x_final[1], 'go-')
plt.show()