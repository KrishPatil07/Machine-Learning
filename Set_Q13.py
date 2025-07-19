# Program to create a set and perform operation
color = {"red", "green", "blue"}
# Add element
color.add("yellow")
print(color)
# Remove element
color.remove("green")
print(color)
# Set operations
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2)) 
print(set1.intersection(set2)) 
print(set1.difference(set2)) 