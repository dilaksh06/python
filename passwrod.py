
import numpy as np

def validate_password(password):
    # Check length
    if len(password) < 8:
        return "Password must be at least 8 characters long."
    
    # Check for at least one uppercase letter
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        return "Password must contain at least one uppercase letter."
    
    # Check for at least one lowercase letter
    has_lower = False
    for char in password:
        if char.islower():
            has_lower = True
            break
    if not has_lower:
        return "Password must contain at least one lowercase letter."
    
    # Check for at least one digit
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        return "Password must contain at least one digit."
    
    # Check for at least one special character
    has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    for char in password:
        if char in special_characters:
            has_special = True
            break
    if not has_special:
        return "Password must contain at least one special character."
    
    return "Password is valid."

# Input from the user
password = input("Enter a password to validate: ")
result = validate_password(password)
print(result)

numbers = [1, 2, 3, 4]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]


print("{:-<10}".format("left"))    # Left-align: "left      "
print("{:>10}".format("right"))   # Right-align: "     right"
print("{:-^10}".format("hello this is dilakshan"))  # Center-align: "  center  "

print(format("-","->20"),"hello",format("-","->20"))



numbers = np.random.randint(0, 101, size=5)  # 101 is exclusive, so 100 is the max value
print(numbers)

