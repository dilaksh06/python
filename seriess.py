import pandas as pd
import numpy as np
a = [10.5, 20.8, 30.5,np.nan,None]
sr=pd.Series(a)
x=sr.drop([0,1])
print(x)
print(sr[sr>20])
data=sr.apply(lambda x:x**2)
print(data)

print(sr.cumsum())

data_get_20=sr>20
print(sr[data_get_20])

print(sr[(sr > 10) & (sr > 20)])


print(sr.isna())
print(sr.notna())
cleaned_data=sr.dropna()
print(cleaned_data)

print("sum =>",sr.sum())

print(sr.fillna(0))

a = [10.5, "fd",20.8, 30.5,np.nan,None]
sr=pd.Series(a)
#data_int=sr.astype(int)
data_int=pd.to_numeric(sr,errors='coerce')
print(data_int)



import pandas as pd

# Sample Series
sr = pd.Series(["apple", "banana", "cherry", "date"])

# Check if strings contain "an"
contains_an = sr.str.contains("an")
print(sr[contains_an])




import pandas as pd

# Sample Series
data = pd.Series([100, 200, 100, 400, 500])

# External grouping key
groups = ['A', 'B', 'A', 'B', 'A']

# Grouping the Series and calculating the sum for each group
grouped = data.groupby(groups).sum()
print(grouped)
print(grouped.agg(['count','sum','mean']))

