import numpy as np

arr = np.arange(0, 11)
print(arr)

print(arr[8])
print(arr[1:5])
print(arr[:5])
print(arr[5:])

new_arr_1 = arr + 100
print(new_arr_1)

new_arr_2 = arr / 2
print(new_arr_2)

print(arr ** 2)

slice_of_arr = arr[0:6]
print(slice_of_arr)

slice_of_arr[:] = 99
print(slice_of_arr)

print(arr)

arr_copy = arr.copy()
arr_copy[:] = 1000
print(arr_copy)

# INDEXING on 2nd array
arr_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
print(arr_2d)
print(arr_2d.shape)

print(arr_2d[1])
print(arr_2d[1][1])
print(arr_2d[1, 1])
print(arr_2d[2, 2])
print(arr_2d[-1, -1])
print(arr_2d[:2, 1:])

arr = np.arange(1, 11)
print(arr > 4)

bool_arr = arr > 4
print(bool_arr)
print(arr[bool_arr])
print(arr[arr > 4])
print(arr[arr == 2])
print(arr[arr <= 6])