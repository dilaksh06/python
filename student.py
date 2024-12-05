class Student():
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def average_marks(self):
        return(round(sum(self.marks)/3,2))
    def is_passing(self):
        if self.average_marks()>50:
            return("stufent s passed")
        else:
            return("student failed")
    def display_info(self):
        return(f"The name is {self.name}, the age is {self.age} and the average mark is {self.average_marks()}")

std1=Student("dilaksn",21,[90,100,100])

print(std1.average_marks())
        
        
print(std1.is_passing())

print(std1.display_info())
