import math

class Shape:
    def area(self):
        raise NotImplementedError("Derived classes need to implement this method.")
    
class Rectangle(Shape):
    def __init__(self, leghth, width):
        self.leghth = leghth
        self.width = width
    
    def area(self):
        return self.leghth * self.width
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
    

