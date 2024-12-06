import pandas as pd
import numpy as np
data=[[1,"sd",25],[2,"ak",36],[3,"jk",26]]
frame=pd.DataFrame(data, columns=["ID","NAME","AGE"])
print(frame)

data2={"ID":[1,2,3],"NAME":["j","k","l"],"AGE":[25,48,36]}
frame2=pd.DataFrame(data2)
print(frame2)


data = {
    'ID': [1, 2, 3, 4, 5],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45],
    'Salary': [50000, 60000, 70000, 80000, 90000]
}

employee=pd.DataFrame(data)
print(employee[employee["Salary"]>60000])
condtion=employee["Age"]>30
print(employee.loc[condtion,['Name','Salary']])
employee["Bonus"]=employee["Salary"]*.8+employee["Salary"]
print(employee)

print("del operatin")

print(employee.drop(1,axis=0))

print("selection of data")
print("\n")
print(employee["Name"])
print("\n")
print(employee.loc[0])
print("\n")
print(employee.iloc[0])
print("\n")
print(employee.loc[1:3,["Name","Age"]])

print(employee["Salary"].mean())
print("\n groupin")
print(employee.groupby("Age")["Salary"].sum())

def salary(salary):
    if(salary>80000):
        return("High")
    elif(salary>60000):
        return("Medium")
    elif(salary>50000):
        return("Low")
    else:
        return("VLOW")

employee["Salary_Level"]=employee["Salary"].apply(salary)

print(employee)


for index,row in employee.iterrows():
    print(f" Name :{row['Name']} , Salary :{row['Salary']} ,Salary : {row['Salary']}")

print("\n")
for c1 in employee.items():
    print(f"c1:{c1}")





arr1 = np.array([[1, 2], [3, 4]])

arr2 = np.array([[5, 6], [7, 8]])

arr = np.stack((arr1, arr2), axis=1)

print(arr)


print(np.array(np.arange(4)),2)
