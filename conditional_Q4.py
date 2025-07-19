# Program to use 'if' conditional statement along with its types
x = int(input(f"Enter a number : "))

#simple if
if x>0:
    print("Greater than zero")

#if else
if x>5:
    print("Greater than 5")
else :
    print("Lesser than 5")

#if elif else 
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
    
#Nested if 
if x>0:
    if x<100:
        print(f"Between 0 - 100")
else:
    pass