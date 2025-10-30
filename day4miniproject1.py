import math

# Base class
class Shape:
    def get_area(self):
        # Common method to be implemented by subclasses
        pass


# Child class for Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


# Child class for Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2


# Child class for Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width


# Example usage
shapes = [
    Circle(5),
    Square(4),
    Rectangle(6, 3)
]

for shape in shapes:
    print(f"{shape.__class__.__name__} Area: {shape.get_area():.2f}")
