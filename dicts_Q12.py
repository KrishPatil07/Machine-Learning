# Program to create a dictionary and perform operations
person = {"name": "Krish", "age": 18, "city": "New York"}
# Access values by key
print(person["name"]) # Output: John
# add new key-value pair
person["email"] = "john@example.com"
print(person) 
# Remove a key-value pair
del person["age"]
print(person)
# Delete whole dictionary
del person
print(person) #result an error , because dictionary's no more