"""
SEABORN — Third-Party Library

Seaborn is a statistical data visualization library built on top of Matplotlib.
It provides:
- high-level plotting functions
- beautiful default styles
- integration with pandas DataFrames
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# BASIC SCATTERPLOT
# ---------------------------------------------------------

tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
plt.show()

# ---------------------------------------------------------
# HISTOGRAM / KDE
# ---------------------------------------------------------

sns.histplot(tips["total_bill"], kde=True)
plt.show()

# ---------------------------------------------------------
# BOXPLOT
# ---------------------------------------------------------

sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()

# ---------------------------------------------------------
# HEATMAP
# ---------------------------------------------------------

corr = tips.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
