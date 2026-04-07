import pandas as pd
df = pd.read_csv('StudentsPerformance.csv')

print(df[['test preparation course', 'reading score', 'writing score']])

print(df.head(100))

print(df.shape)

print(df.info())

print(df.dtypes)