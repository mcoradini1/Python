'''
matplot is a python plotting library for publication-quality figures, a large library with loads of functions.
pyplot is just one of the modules of matplotlib that works like mathlab, being so useful when working with interactive
work for exploration of dataset.

import matplotlib.pyplot as plt (need to install it)
'''
import matplotlib.pyplot as plt
import numpy as np

# PLOT USING LIST ------------------------------------------------------------------------------------------------------
plt.plot([0,1,4,9,16])
plt.show() #if i remove from here, i will have 2 in the same (a bit bug..)

# PLOT USING ARRAYS ----------------------------------------------------------------------------------------------------
x = np.linspace(0,10,20) #create a vector in my one dimensional array
y = x ** 2

plt.plot(x,y)
plt.show()

y2 = x ** 1.5

#CUSTOMIZING PLOTS -----------------------------------------------------------------------------------------------------
plt.plot(x,y, 'bo', linewidth = 2, markersize = 4) #blue, circles, without line
plt.show()

plt.plot(x,y, 'gs-', linewidth = 2, markersize = 4) #green, squares, and line
plt.show()

plt.plot(x,y, 'rd-', linewidth = 2, markersize = 30) #I am asking to use red, diamonds, and line -
plt.show()



