"""
PYTORCH — Third-Party Library

Machine Learning
PyTorch is a deep learning framework known 5.1 - For:
- dynamic computation graphs
- intuitive tensor operations
- neural networks

This example shows:
- creating tensors
- building a simple linear model
- training with gradient descent
"""

import torch

# ---------------------------------------------------------
# DATA
# ---------------------------------------------------------

x = torch.tensor([[0.0], [1.0], [2.0], [3.0]])
y = torch.tensor([[1.0], [3.0], [5.0], [7.0]])  # y = 2x + 1

# ---------------------------------------------------------
# MODEL
# ---------------------------------------------------------

model = torch.nn.Linear(1, 1)

# ---------------------------------------------------------
# LOSS & OPTIMIZER
# ---------------------------------------------------------

loss_fn = torch.nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

# ---------------------------------------------------------
# TRAINING LOOP
# ---------------------------------------------------------

for epoch in range(200):
    y_pred = model(x)
    loss = loss_fn(y_pred, y)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------

print(model(torch.tensor([[10.0]])))
