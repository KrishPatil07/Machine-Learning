# Program to perform File Handling Operations

# Open a file for reading
file = open('KrishP.txt', 'r') #file has 'Hello , Krish Patil!' before running 
content = file.read()
print(content)
file.close()
# Open a file for writing
file = open('KrishP.txt', 'w')
file.write('Hello, World!\n')
file.close()
# Open a file for appending
file = open('KrishP.txt', 'a')
file.write('This is an appended line.\n')
file.close()