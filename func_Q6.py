#program to use user-defined functions

#function with parameter , no return value 
def greet(name):
    print(f"Hello, {name}!")
greet("KRISH")

#function with parameters and a return value 
def add(x, y):
    return x + y
result = add(7, 3)
print(result)