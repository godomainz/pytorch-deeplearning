import numpy as np

# 2. Create an array of 10 zeros
arr_zeroes = np.zeros(10)
print(arr_zeroes)

# 3. Create an array of 10 ones
arr_ones = np.ones(10)
print(arr_ones)

# 4. Create an array of 10 fives
arr_fives = np.ones(10) * 5
print(arr_fives)

# 5. Create an array of the integers from 10 to 50
arr_ten_to_fifty = np.arange(10, 51)
print(arr_ten_to_fifty)

# 6. Create an array of all the even integers from 10 to 50
arr_even_ints = np.arange(10, 51, 2)
print(arr_even_ints)

# 7. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3_by_3 = np.arange(0, 9).reshape(3, 3)
print(matrix_3_by_3)

# 8. Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print(identity_matrix)

# 9. Use NumPy to generate a random number between 0 and 1
random_num = np.random.rand()
print(random_num)

# 10. Use NumPy to generate an array of 25 random numbers sampled from a standard normal distribution
array_std_normal_distribution = np.random.normal(size=25)
print(array_std_normal_distribution)

# 11. Create the following matrix:
my_matrix = np.arange(1, 101).reshape(10, 10) / 100
print(my_matrix)

# 12. Create an array of 20 linearly spaced points between 0 and 1
lin_space = np.linspace(0, 1, 20)
print(lin_space)

# Numpy Indexing and Selection
mat = np.arange(1,26).reshape(5,5)
print(mat)

# 13. Write code that reproduces the output shown below.
# array([[12, 13, 14, 15],
#        [17, 18, 19, 20],
#        [22, 23, 24, 25]])

print(mat[2:,1:])

# 14. Write code that reproduces the output shown below.
# 20
print(mat[3,4])

# 15. Write code that reproduces the output shown below.
# array([[ 2],
#        [ 7],
#        [12]])
print(mat[0:3, 1:2])

# 16. Write code that reproduces the output shown below.
# array([21, 22, 23, 24, 25])
print(mat[4])

# 17. Write code that reproduces the output shown below.
# array([[16, 17, 18, 19, 20],
#        [21, 22, 23, 24, 25]])
print(mat[3:])

# 18. Get the sum of all the values in mat
print(mat.sum())

# 19. Get the standard deviation of the values in mat
print(mat.std())

# 20. Get the sum of all the columns in mat
print(mat.sum(axis=0))

# We worked a lot with random data with numpy, but is there a way we can insure that we always get the same random numbers?
np.random.seed(101)