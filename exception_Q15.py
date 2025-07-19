# Program to use Exception Handling 
# Single Exception
try:
    x = 2 / 0   
except ZeroDivisionError:
    print("Cannot divide by zero!")
# Multiple Exceptions
try:
    x = "6" / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except TypeError:
    print("Invalid type!")
# Automatic error detection ; to print any type of error occured
try:
    y="ab"+2
except Exception as e:
    print(f"An error occurred: {e}")