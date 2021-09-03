import pandas as pd

df = pd.read_csv(filepath_or_buffer='bank.csv')

# TASK: Display the first 5 rows of the data set
print(df[0:6])
print(df.iloc[0:6])

# TASK: What is the average (mean) age of the people in the dataset?
print(df['age'].mean())

# TASK: What is the marital status of the youngest person in the dataset?
print(df.loc[df['age'].min(), 'marital'])
print(df.loc[df['age'].idxmin(), 'marital'])
print(df.iloc[df['age'].idxmin()]['marital'])

# TASK: How many unique job categories are there?
print(len(df['job'].unique()))

# TASK: How many people are there per job category? (Take a peek at the expected output)
print(df['job'].value_counts())

# TASK: What percent of people in the dataset were married?
print(df['marital'].value_counts()['married']/len(df) * 100)

# TASK: Using pandas .apply() method, create a new column called "marital code". This column will only contained a shortened code of the possible marital status first letter. (For example "m" for "married" , "s" for "single" etc... See if you can do this with a lambda expression. Lots of ways to do this one!

# Solution 1
def get_first_letter(word: str):
    return word[0]
df['marital code'] = df['marital'].apply(get_first_letter)
print(df)

# Solution 2
df['marital code'] = df['marital'].apply(lambda status: status[0])
df.head()
print(df)

# TASK: What was the longest lasting duration?
print(df['duration'].max())

# TASK: What is the most common education level for people who are unemployed?
print(df[df['job']=='unemployed']['education'].value_counts())

# TASK: What is the average (mean) age for being unemployed?
print(df[df['job']=='unemployed']['age'].mean())