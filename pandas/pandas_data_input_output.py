import pandas as pd

df = pd.read_csv(filepath_or_buffer='example.csv')
newdf = df[['a', 'b']]

newdf.to_csv('mynew.csv', index=False)

df = pd.read_excel('Excel_Sample.xlsx', sheet_name='Sheet1')
df = df.drop('Unnamed: 0', axis=1)

mylist_of_tables = pd.read_html('https://en.wikipedia.org/wiki/Table_(information)')
print(type(mylist_of_tables))
print(len(mylist_of_tables))
df = mylist_of_tables[0]