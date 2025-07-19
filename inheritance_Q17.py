# Program to implement inheritance
class Animal: #Base Class
    def __init__(self, name):
        self.name = name
    def sound(self):
        print("The animal made a sound.")

class Dog(Animal): #Child Class
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def sound(self):
        print("The dog barks")

my_dog = Dog("Fido", "Golden Retriever")
my_dog.sound() # Output: The dog barks.