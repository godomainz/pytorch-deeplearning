import torch
import numpy as np

# Set the random seed for NumPy and PyTorch both to "42"
np.random.seed(42)
torch.manual_seed(42)

# Create a NumPy array called "arr" that contains 6 random integers between 0 (inclusive) and 5 (exclusive)
arr =np.random.randint(0, 5, 6)
print(arr)

# Create a tensor "x" from the array above
x = torch.tensor(arr)
print(x)

# Change the dtype of x from 'int32' to 'int64'
x = x.type(torch.int64)
print(x.type())

# Reshape x into a 3x2 tensor
x = x.reshape(3, 2)
print(x)

# Return the right-hand column of tensor x
print(x[:, 1:])

# Without changing x, return a tensor of square values of x
print(torch.square(x))

# Create a tensor "y" with the same number of elements as x, that can be matrix-multiplied with x
y = torch.randint(0, 5, (2,3))
print(y)

# Find the matrix product of x and y
print(torch.mm(x, y))