# creational/shape_factory.py

from abc import ABC, abstractmethod
from typing import Protocol, List

class Shape(Protocol):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self) -> float:
        """Calculate the perimeter of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Compute the area of the circle."""
        return 3.14159 * (self.radius ** 2)

    def perimeter(self) -> float:
        """Compute the perimeter of the circle."""
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Compute the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Compute the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, *args: float) -> Shape:
        """Factory method to create shapes based on provided type."""
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            if len(args) != 1 or args[0] <= 0:
                raise ValueError("Circle requires a positive radius.")
            return Circle(args[0])
        elif shape_type == 'rectangle':
            if len(args) != 2 or args[0] <= 0 or args[1] <= 0:
                raise ValueError("Rectangle requires positive width and height.")
            return Rectangle(args[0], args[1])
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

# Sample Usage
if __name__ == "__main__":
    shapes: List[Shape] = []
    
    try:
        circle = ShapeFactory.create_shape('circle', 5)
        rectangle = ShapeFactory.create_shape('rectangle', 4, 6)
        
        shapes.append(circle)
        shapes.append(rectangle)

        for shape in shapes:
            print(f"{shape.__class__.__name__} - Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    
    except ValueError as e:
        print(e)