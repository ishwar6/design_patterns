# creational/factory.py

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius):
        """Initialize a Circle with a given radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, side_length):
        """Initialize a Square with a given side length."""
        self.side_length = side_length

    def area(self):
        """Calculate the area of the square."""
        return self.side_length ** 2

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type, *args):
        """Create a shape based on the specified type."""
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'square':
            return Square(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Sample usage
if __name__ == "__main__":
    circle = ShapeFactory.create_shape('circle', 5)
    print(f"Circle Area: {circle.area()}")  # Output: Circle Area: 78.53975

    square = ShapeFactory.create_shape('square', 4)
    print(f"Square Area: {square.area()}")  # Output: Square Area: 16