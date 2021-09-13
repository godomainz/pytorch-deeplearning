import torch
import numpy as np
import matplotlib.pyplot as plt
import torch.nn as nn

X = torch.linspace(1, 50, 50).reshape(-1, 1)
print(X)

torch.manual_seed(71)
e = torch.randint(-8, 9,(50, 1), dtype=torch.float)
print(e)

y = 2*X + 1 + e
print(y.shape)
plt.scatter(X.numpy(), y.numpy())
plt.show()

torch.manual_seed(59)
model = nn.Linear(in_features=1, out_features=1)
print(model.weight)
print(model.bias)


class Model(nn.Module):

    def __init__(self, in_features, out_featues):
        super().__init__()
        self.linear = nn.Linear(in_features, out_featues)

    def forward(self, x):
        y_pred = self.linear(x)
        return y_pred