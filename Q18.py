# Program to implement Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return 3.14 * self.r ** 2
    
class Rect(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h
    def area(self):
        return self.w * self.h
    
shapes = [Circle(2), Rect(4, 8)]
for shape in shapes:
    print(shape.area())