import numpy as np

print(np.random.rand())
print(np.random.rand(4))
print(np.random.rand(5,5))
print(np.random.randn(10))

# here loc = mean, scale = standard deviation
print(np.random.normal(loc=1, scale=2, size=5))

print(np.random.randint(1, 100, 10))
np.random.seed(101)
print(np.random.rand(4))

arr = np.arange(25)
print(arr)

randarr = np.random.randint(0, 50, 10)
print(randarr)

print(arr.reshape(5, 5))

print(randarr.max())
print(randarr.min())
print(randarr.argmax())
print(randarr.argmin())

print(randarr.dtype)