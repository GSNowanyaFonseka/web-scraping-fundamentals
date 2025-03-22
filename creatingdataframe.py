# creating dataframes
import pandas as pd

# creating a python dictionary (keys maps with python list)
data = {
    'name' : ['John','Alice'], 
    'Age':[25, 30]
    }

# convert pythondictionary into dataframe
df = pd.DataFrame(data)

# display dataframe in tabular structure
print(df)