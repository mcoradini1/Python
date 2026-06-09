"""
TENSORFLOW — Third-Party Library

Machine Learning
TensorFlow is a deep learning framework used 5.1 - For:
- neural networks
- image classification
- natural language processing
- large-scale machine learning

This example shows:
- creating a simple neural network
- training it on dummy data
"""

import tensorflow as tf
import numpy as np

# ---------------------------------------------------------
# CREATE DUMMY DATA
# ---------------------------------------------------------

# y = 2x + 1 (simple linear relationship)
x = np.array([0, 1, 2, 3, 4], dtype=float)
y = 2 * x + 1

# ---------------------------------------------------------
# BUILD A SIMPLE MODEL
# ---------------------------------------------------------

model = tf.keras.Sequential([
    tf.keras.layers.Dense(units=1, input_shape=[1])
])

model.compile(optimizer="sgd", loss="mean_squared_error")

# ---------------------------------------------------------
# TRAIN THE MODEL
# ---------------------------------------------------------

model.fit(x, y, epochs=200, verbose=0)

# ---------------------------------------------------------
# PREDICT
# ---------------------------------------------------------

print(model.predict([10.0]))
