# dataframe operations
import pandas as pd

df = pd.read_csv('example.csv')

# summary of the dataset
df.info()

# statistical summary
desc = df.describe()
print(desc)

# first 5 rows
rows = df.head(5) 
print(rows)

# column names
columns = df.columns
print(columns)
