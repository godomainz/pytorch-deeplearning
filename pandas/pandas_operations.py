import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
df.head()
print(df.head())

print(df['col2'].unique())
print(df['col2'].nunique())
print(df['col2'].value_counts())

newdf = df[(df['col1'] > 2) & (df['col2'] == 444)]
print(newdf)


def times_two(number):
    return number * 2

print(times_two(4))

print(df.apply(times_two))
df['new'] = df['col1'].apply(times_two)
print(df)

del df['new']

print(df.columns)
print(df.index)
print(df.info())
print(df.describe())
print(df.sort_values(by='col2'))
print(df.sort_values(by='col2', ascending=False))