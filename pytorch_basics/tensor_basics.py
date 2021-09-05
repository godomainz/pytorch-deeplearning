import torch
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(arr.dtype)
print(type(arr))

x = torch.from_numpy(arr)
print(x)
print(type(x))

print(torch.as_tensor(arr))
print(x.dtype)

arr2d = np.arange(0.0, 12.0)
arr2d = arr2d.reshape(4, 3)
print(arr2d)

x2 = torch.from_numpy(arr2d)
print(x2)

arr[0] = 99
print(arr)
print(x)

my_arr = np.arange(0, 10)
print(my_arr)

my_tensor = torch.tensor(my_arr)
my_other_tensor = torch.from_numpy(my_arr)

print(my_tensor)
print(my_other_tensor)

my_arr[0] = 9999
print(my_arr)

print(my_other_tensor)
print(my_tensor)