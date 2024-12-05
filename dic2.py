dictionary={"Brand": "Toyota",
"Model": "Corolla",
"Year": 2020}

dictionary["color"]="Red"
print(dictionary.keys())
print("engine" in dictionary)

numbers = (10, 20, 30, 40, 50, 60)
print(numbers[0])
print(numbers[len(numbers)-1])
print(numbers[1:4])
print(30 in numbers)
print(numbers.count(40))
      
    
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1|set2)
print(set1&set2)
print(set1-set2)
print(set1.isdisjoint(set2))


students = {
    "John": {"Math": 90, "Science": 85, "English": 88},
    "Jane": {"Math": 92, "Science": 78, "English": 94},
    "Jake": {"Math": 85, "Science": 89, "English": 82}
}

subjects = ["Math", "Science", "English"]


print(students.keys())

for x,y in students.items():
    print("the student name is : ",x, ", the sum fo the marsk are", sum(y.values()))

students["jack"]={"Math": 88, "Science": 80, "English": 91}














