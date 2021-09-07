import torch
import numpy as np

new_arr = np.array([1, 2, 3])
print(new_arr.dtype)

print(torch.tensor(new_arr))
my_tensor = torch.Tensor(new_arr)
print(my_tensor)
print(my_tensor.dtype)

print(torch.empty(4, 2))
print(torch.zeros(4, 3))
print(torch.zeros(4, 3, dtype=torch.int32))
print(torch.ones(4, 3))
print(torch.arange(0, 18, 2))
print(torch.arange(0, 18, 2).reshape(3, 3))
print(torch.linspace(0, 18, 12).reshape(3, 4))

print(torch.tensor([1, 2, 3]))

my_tensor = torch.tensor([1, 2, 3])
print(my_tensor.dtype)

my_tensor = my_tensor.type(torch.int32)
print(my_tensor.dtype)

print(torch.rand(4, 3))
print(torch.randn(4, 3))
print(torch.randint(low=0, high=10, size=(5, 5)))

x = torch.zeros(2, 5)
print(x)

print(torch.rand_like(x))
print(torch.randn_like(x))
print(torch.randint_like(x, low=0, high=11))

torch.manual_seed(42)
print(torch.rand(2, 3))