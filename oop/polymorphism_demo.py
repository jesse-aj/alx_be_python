import math
class Shape:
    def area(self):
        raise NotImplementedError
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        results = self.length * self.width
        return results

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
       

    def area(self):
        results = math.pi * self.radius ** 2
        return results


