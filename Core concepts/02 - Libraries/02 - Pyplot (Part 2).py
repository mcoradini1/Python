
import matplotlib.pyplot as plt
import numpy as np

#AXIS POSITIONING-------------------------------------------------------------------------------------------------------
x = np.linspace(0,10,20)
y = x ** 2
y2 = x ** 1.5

plt.plot(x,y, 'bo-', linewidth = 2, markersize = 4)
plt.plot(x,y2, 'gs-', linewidth = 2, markersize = 4)
plt.xlabel('$x$')
plt.ylabel('$y$')
plt.axis([-10, 10.5, -5, 105])                    #([xmin, xmax, ymin, ymax])
plt.show()

#LABELING --------------------------------------------------------------------------------------------------------------
plt.plot(x,y, 'bo-', linewidth = 2, markersize = 4, label = 'First')
plt.plot(x,y2, 'gs-', linewidth = 2, markersize = 4, label = 'Second')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

#plt.savefig('myplot.pdf')  #decide the type that I want

plt.show()


#LOGARITHMIC PLOT  -----------------------------------------------------------------------------------------------------
'''log is default to 10. log 100 is 2
plt.semilogx() x
plt.semilogy() y 
plt.loglog() both
np.logspace(-1,1, 40)

y = x ** alpha
log y = alpha log x
y' = alpha x'

before it was an parabola, but we change it to linear where alpha is the inclination of line
'''

#USING LOGARITHMIC AXES ------------------------------------------------------------------------------------------------
x2 = np.logspace(-1,1, 40)
y2 = x2 ** 2
x3 = x2 ** 1.5
y3 = x3 ** 2


plt.loglog(x2,y2, 'bo-', linewidth = 2, markersize = 4, label = 'x1')
plt.loglog(x3,y3, 'gs-', linewidth = 2, markersize = 4, label = 'y1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show()