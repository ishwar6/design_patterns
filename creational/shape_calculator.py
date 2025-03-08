# creational/shape_factory.py

from abc import ABC, abstractmethod
from typing import Dict

class Shape(ABC):
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
        """Calculate the area of the circle."""
        import math
        return math.pi * (self.radius ** 2)

    def perimeter(self) -> float:
        """Calculate the perimeter (circumference) of the circle."""
        import math
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

class ShapeFactory:
    @staticmethod
    def create_shape(shape_type: str, **kwargs) -> Shape:
        """Create a shape object based on the shape type."""
        shape_mapping: Dict[str, Shape] = {
            'circle': Circle,
            'rectangle': Rectangle
        }
        
        shape_class = shape_mapping.get(shape_type.lower())
        if not shape_class:
            raise ValueError(f"Unknown shape type: {shape_type}")

        return shape_class(**kwargs)

if __name__ == '__main__':
    # Example Usage
    try:
        circle = ShapeFactory.create_shape('circle', radius=5)
        print(f"Circle Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")

        rectangle = ShapeFactory.create_shape('rectangle', width=4, height=3)
        print(f"Rectangle Area: {rectangle.area():.2f}, Perimeter: {rectangle.perimeter():.2f}")
    except ValueError as e:
        print(e)