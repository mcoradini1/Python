"""
PLOTLY — Third-Party Library

Plotly is an interactive plotting library.
Plots can be zoomed, hovered, and exported as HTML.
"""

import plotly.express as px
import numpy as np
import pandas as pd

# ---------------------------------------------------------
# SCATTER PLOT
# ---------------------------------------------------------

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")
fig.show()

# ---------------------------------------------------------
# LINE PLOT
# ---------------------------------------------------------

x = np.linspace(0, 10, 100)
y = np.sin(x)

fig = px.line(x=x, y=y, title="Sine Wave")
fig.show()

# ---------------------------------------------------------
# BAR CHART
# ---------------------------------------------------------

fig = px.bar(df, x="species", y="petal_length")
fig.show()
