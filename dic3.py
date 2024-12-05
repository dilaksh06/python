marks={"maths":0,"science":0,"english":0}
students={}
while(False):
    print ("enter 1 to continue add data\nenter 2 diplay data\nenter 3 to diplay the marks of a specific student\nenter 4 to find average marks of each students\nenter 5 to exit")
    choice=int(input("enter your choic :"))
    if (choice==1):
        
        name=input("enter the student anme :")
        maths=int(input("enter the makrs for maths : "))
        science=int(input("enter the makrs for maths : "))
        english=int(input("enter the makrs for maths : "))
        marks["maths"]=maths
        marks["science"]=science
        marks["english"]=english
        if name not in students:
            students[name]=marks
    elif(choice==2):
        print(students)
    elif(choice==3):
        name=input("enter the name of the student :")
        if name in students:
            print(students[name])
    elif(choice==4):
        for x,y in students.items():
            print(f"the average mark of the student \"{x}\" is :{sum(y.values())/3}")
        
    elif(choice==5):
        break
        
    

for x in range(20,8,-2):
    print(x)

name=["d","b","c"]
age=[18,45,80]

for name,age in zip(name,age):
    if (age>18):
        print("the name is :",name,"the age is :",age)

x="dilakshan"

bc=["c","afg","jk"]
bc.sort()
print(bc)



"""Palindrome Checker: Write a program to check if a string is a palindrome (reads the same forwards and backwards).

String Formatter: Create a string that contains the name and age of a person using an f-string. For example, "John is 25 years old"."""

x="121"
y=x[: :-1]
print (y)
if (x.isdigit()):
    if(x==y):
        print("it is palindrom")
    
#John is 25 years old
name="jhon"
age=25
print(f"{name} is {age} years old")

c="World Hello dilakshan"
x=c.split(" ")
print(x)
z=""
for b in x:
    z=b+" "+z
print(z)


string=input("enter the string : ")
string=string.lower()
print(string)
vowels="aeiou"
count=0
for x in string:
    for v in vowels:
        if(x==v):
            count+=1
print("the number fo vowels are : ",count)
print(string.capitalize())

for x in string:
    if(x.isdigit()):
        print(x)

sentence = "Hello World dilakshan"
words = sentence.split()  # Split the sentence into words
reversed_sentence = " ".join(reversed(words))  # Reverse the words and join them back
print(reversed_sentence)  # Output: World Hello

