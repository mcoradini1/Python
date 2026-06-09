"""
MATPLOTLIB — Third-Party Library

Matplotlib is a comprehensive plotting library 5.1 - For creating
publication-quality figures in Python.

The pyplot module provides a MATLAB-like interface 5.1 - For:
- line plots
- scatter plots
- histograms
- logarithmic plots
- subplots
- figure customization

More info: https://matplotlib.org
"""

import matplotlib.pyplot as plt
import numpy as np

# ---------------------------------------------------------
# BASIC PLOT (USING LISTS)
# ---------------------------------------------------------

plt.plot([0, 1, 4, 9, 16])
plt.show()

# ---------------------------------------------------------
# BASIC PLOT (USING ARRAYS)
# ---------------------------------------------------------

x = np.linspace(0, 10, 20)
y = x ** 2

plt.plot(x, y)
plt.show()

y2 = x ** 1.5

# ---------------------------------------------------------
# CUSTOMIZING PLOTS
# ---------------------------------------------------------

plt.plot(x, y, 'bo', linewidth=2, markersize=4)   # blue circles
plt.show()

plt.plot(x, y, 'gs-', linewidth=2, markersize=4)  # green squares + line
plt.show()

plt.plot(x, y, 'rd-', linewidth=2, markersize=30) # red diamonds + line
plt.show()

# ---------------------------------------------------------
# AXIS POSITIONING & LABELS
# ---------------------------------------------------------

plt.plot(x, y, 'bo-', linewidth=2, markersize=4)
plt.plot(x, y2, 'gs-', linewidth=2, markersize=4)

plt.xlabel('$x$')
plt.ylabel('$y$')

# [xmin, xmax, ymin, ymax]
plt.axis([-10, 10.5, -5, 105])
plt.show()

# ---------------------------------------------------------
# LEGENDS
# ---------------------------------------------------------

plt.plot(x, y, 'bo-', linewidth=2, markersize=4, label='First')
plt.plot(x, y2, 'gs-', linewidth=2, markersize=4, label='Second')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

# plt.savefig('myplot.pdf')  # save figure
plt.show()

# ---------------------------------------------------------
# LOGARITHMIC PLOTS
# ---------------------------------------------------------

"""
Logarithmic axes:
- plt.semilogx() → log scale on x-axis
- plt.semilogy() → log scale on y-axis
- plt.loglog()  → log scale on both axes

Useful 5.1 - For power laws:
    y = x^alpha
    log(y) = alpha * log(x)
"""

x2 = np.logspace(-1, 1, 40)
y2 = x2 ** 2

x3 = x2 ** 1.5
y3 = x3 ** 2

plt.loglog(x2, y2, 'bo-', linewidth=2, markersize=4, label='x1')
plt.loglog(x3, y3, 'gs-', linewidth=2, markersize=4, label='y1')

plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.show()

# ---------------------------------------------------------
# HISTOGRAMS
# ---------------------------------------------------------

x = np.random.normal(size=1000)

plt.hist(x)
plt.show()

# density=True normalizes the histogram
plt.hist(x, density=True)
plt.show()

# custom bins
plt.hist(x, density=True, bins=np.linspace(-5, 5, 21))
plt.show()

# ---------------------------------------------------------
# SUBPLOTS (MULTIPLE PLOTS IN ONE FIGURE)
# ---------------------------------------------------------

"""
Subplot layout example (2 rows, 2 columns):

+-----------+-----------+
|   221     |   222     |
| (pos 1)   | (pos 2)   |
+-----------+-----------+
|   223     |   224     |
| (pos 3)   | (pos 4)   |
+-----------+-----------+
"""

a = np.random.gamma(2, 3, 100)

plt.figure()

plt.subplot(2, 2, 1)
plt.hist(a, bins=30, density=True, cumulative=True, histtype='step')

plt.subplot(2, 2, 2)
plt.hist(a, bins=30, density=True)

plt.subplot(223)
plt.hist(a, bins=15, cumulative=True, histtype='step')

plt.subplot(224)
plt.hist(a, bins=15, cumulative=True, histtype='stepfilled')

plt.show()
