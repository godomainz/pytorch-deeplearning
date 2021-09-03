import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
rand_mat = randn(5, 4)

df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())

print(df > 0)

df_bool = df > 0
print(df[df_bool])

print(df['W'] > 0)
print(df[df['W'] > 0])

print(df[df['W'] > 0]['Y'])

print(df[(df['W'] > 0) & (df['Y'] > 1)])

print(df.reset_index())

new_ind = 'CA NY WY OR CO'.split()
print(new_ind)

df['States'] = new_ind
print(df)

df.set_index('States', inplace=True)
print(df)

print(df.info())
print(df.dtypes)
print(df.describe())

ser_w = df['W'] > 0
print(ser_w.value_counts())

print(sum(ser_w))
print(len(ser_w))
