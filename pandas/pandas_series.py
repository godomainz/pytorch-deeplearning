import numpy as np
import pandas as pd

labels = ["a", "b", "c"]
mylist = [10, 20, 30]
arr = np.array(mylist)
print(arr)

d = {'a': 10, 'b': 20, 'c': 30}
print(d)

print(pd.Series(data=mylist))
print((pd.Series(arr)))

print(pd.Series(data=arr, index=labels))
print(pd.Series(data=[10, 'a', 4.4]))

ser1 = pd.Series(data=[1, 2, 3, 4], index=['USA', 'Germany', 'USSR', 'Japan'])
print(ser1)
print(ser1['USA'])

ser2 = pd.Series(data=[1, 4, 5, 6], index=['USA', 'Germany', 'Italy', 'Japan'])
print(ser2)

print(ser1 + ser2)