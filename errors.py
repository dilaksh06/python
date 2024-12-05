# Example: IndexError
my_list = [1, 2, 3]
try:
    print(my_list[5])  # Accessing an index that doesn't exist
except IndexError:
    print("Error: Index out of range!")

# Example: NameError
try:
    print(unknown_variable)  # Variable not defined
except NameError:
    print("Error: Variable not defined!")

"""
Write a program to handle a ZeroDivisionError
when dividing two numbers provided by the user.
Create a program that takes an input string
and tries to convert it into an integer.
Use a try block to handle a ValueError if the conversion fails.
Write a program to open a file named "example.txt".
Handle the FileNotFoundError if the file does not exist."""

try:
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    z = x / y
    success = True  # Indicate success
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    success = False  # Indicate failure
else:
    print("The result of the division is:", z)
finally:
    if success:
        print("Operation completed successfully.")
    else:
        print("Operation failed.")


"""Create a program that takes an input string and tries to convert
it into an integer. Use a try block to handle a ValueError if the conversion fails."""



try:
    x=input("enter a text")
    y=int(x)
except ValueError:
    print("cannot change and it is value error")
else:
    print(y)


"""Write a program to open a file named "example.txt". Handle the FileNotFoundError if the file does not exist."""

try:
    file=open("a.txt","r")
    content=file.read()
    file.close()
except FileNotFoundError:
    print("file doesnot exit")
else:
    print(content)


"""Write a program that accesses a list element by index provided by the user. Handle IndexError if the index is out of range."""

try:
    x=[1,2,3,4,5]
    print(x[8])
except IndexError:
    print("index is out of range")
else:
    print(x[8])


"""Create a program that checks if a key exists in a dictionary. If not, catch the KeyError and display a message."""


try:
    dictt={"a":5}
    print(dictt["c"])
except KeyError:
    print("invalide key")
else:
    print("it will not execute")



try:
    # Taking two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing division
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Invalid input. Please enter numeric values!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

