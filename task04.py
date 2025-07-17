import math

class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.name = "Circle"  
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.name = "Rectangle"  
    def area(self):
        return self.width * self.height

shapes = [Circle(5), Rectangle(4, 6)]
for s in shapes:
    print(f"{s.name} area: {s.area():.2f}")
