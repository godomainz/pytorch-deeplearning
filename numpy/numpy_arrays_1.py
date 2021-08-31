import numpy as np

mylist = [1, 2, 3]
print(type(mylist))
print(np.array(mylist))
print(type(mylist))
arr = np.array(mylist)

mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mymatrix = np.array(mylist)
print(mymatrix)
print(mymatrix.shape)

print(np.arange(0, 10, 2))

print(np.zeros(5))
print(np.zeros((4, 10)))
print(np.ones((4, 10)))
print(np.ones((4, 10))+4)
print(np.ones((4, 10))*4)
print(np.linspace(0, 10, 3))
print(np.eye(5))