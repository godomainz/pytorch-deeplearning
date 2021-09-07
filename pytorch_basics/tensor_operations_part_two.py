import torch

a = torch.tensor([1., 2., 3.])
b = torch.tensor([4., 5., 6.])

print(a * b)

print(a.dot(b))

a = torch.tensor([[0, 2, 4], [1, 3, 5]])
print(a)

b = torch.tensor([[6, 7], [8, 9], [10, 11]])
print(b)

print(a.shape)
print(b.shape)

print(torch.mm(a, b))

print(a @ b)

x = torch.tensor([2., 3., 4., 5.])
print(x.norm())

print(x.numel())

print(len(x))
print(len(a))
print(a.numel())