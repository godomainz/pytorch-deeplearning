import torch

x = torch.arange(6).reshape(3, 2)
print(x)

print(x[1, 1])
print(type(x[1, 1]))
print(x[:, 1])
print(x[:, 1:])

x = torch.arange(10)
print(x)


print(x.view(2, 5))


print(x.reshape(2, 5))
print(x)

x = x.reshape(2, 5)
print(x)

x = torch.arange(10)
print(x.shape)

print(x.view(2, 5))

z = x.view(2, 5)
print(z)

print(x)
x[0] = 9999
print(x)

print(z)

x = torch.arange(10)
print(x.view(2, -1))
print(x.view(-1, 5))
print(x.view(-1))

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])
print(a.dtype)
print(b.dtype)

print(a + b)

print(torch.add(a, b))

print(a.mul(b))
print(a)

print(a.mul_(b))
print(a)