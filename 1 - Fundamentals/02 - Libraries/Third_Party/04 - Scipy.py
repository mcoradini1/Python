"""
SCIPY — Third-Party Library

SciPy builds on NumPy and provides:
- optimization
- integration
- interpolation
- statistics
- signal processing
"""

import numpy as np
from scipy import optimize, stats, integrate

# ---------------------------------------------------------
# ROOT FINDING
# ---------------------------------------------------------

def f(x):
    return x**3 - 5*x + 1

root = optimize.root_scalar(f, bracket=[-3, 3])
print(root.root)

# ---------------------------------------------------------
# NUMERICAL INTEGRATION
# ---------------------------------------------------------

result, error = integrate.quad(lambda x: np.sin(x), 0, np.pi)
print(result)

# ---------------------------------------------------------
# STATISTICS (NORMAL DISTRIBUTION)
# ---------------------------------------------------------

mean, std = 0, 1
print(stats.norm.pdf(0, mean, std))
print(stats.norm.cdf(1.96, mean, std))
