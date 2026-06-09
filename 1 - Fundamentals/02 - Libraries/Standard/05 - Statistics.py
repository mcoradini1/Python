"""
STATISTICS — Python Standard Library

Provides basic statistical functions.
"""

import statistics as stats

data = [1, 2, 3, 4, 5, 6]

# ---------------------------------------------------------
# BASIC STATISTICS
# ---------------------------------------------------------

print(stats.mean(data))
print(stats.median(data))
print(stats.mode([1, 1, 2, 3]))
print(stats.stdev(data))
