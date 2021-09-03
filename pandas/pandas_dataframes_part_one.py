import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)
rand_mat = randn(5, 4)
print(rand_mat)

df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)

print(df['W'])
mylist = ['W', 'Y']
print(df[mylist])

df['NEW'] = df['W'] + df['Y']

df.drop('NEW', axis=1, inplace=True)

df.drop('A', inplace=True)

df = pd.DataFrame(data=rand_mat, index='A B C D E'.split(), columns='W X Y Z'.split())
print(df.loc['A'])
print(df.iloc[2])

print(df.loc[['A', 'E']])
print(df.iloc[[0, 3]])

print(df.loc[['A', 'B']][['Y', 'Z']])
print(df.loc[['A', 'B'], ['Y', 'Z']])