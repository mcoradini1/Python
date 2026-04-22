import numpy as np
import matplotlib.pyplot as plt

x = np.random.normal(size=1000) #by default uses 10 bins evenly spaced...
plt.hist(x)
plt.show()

plt.hist(x, density=True) #density is the old normed (instead of number of observation we have proportion)
plt.show()

plt.hist(x, density=True, bins = np.linspace(-5,5,21))
#we determined 20 bins within the size -5 and 5 (always need 1 extra... because of start and end...)
#for example for 1 column its need 1 star and 1 end.
plt.show()


'''

#gamma distribution (continuous probability of increase,starts at 0 and goes to positive infinite)

#pltfunction subplot that allows us to have more plots in one figure

Example of 2 rows and 2 columns (4 plots)

+-----------+-----------+
|   221     |   222     |
| (pos 1)   | (pos 2)   |
+-----------+-----------+
|   223     |   224     |
| (pos 3)   | (pos 4)   |
+-----------+-----------+

'''

a = np.random.gamma(2,3,100)
plt.figure()
plt.subplot(2,2,1)
plt.hist(a, bins = 30, density = True, cumulative = True, histtype= 'step')
plt.subplot(2,2,2)
plt.hist(a, bins = 30, density = True)
plt.subplot(223)
plt.hist(a, bins = 15, cumulative = True, histtype= 'step')
plt.subplot(224)
plt.hist(a, bins = 15, cumulative = True, histtype= 'stepfilled')
plt.show()




