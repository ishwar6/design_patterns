# creational/shape_factory.py

from abc import ABC, abstractmethod
from typing import Dict

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * (self.radius ** 2)

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

class ShapeFactory:
    shapes: Dict[str, Shape] = {}

    @staticmethod
    def register_shape(shape_type: str, shape_instance: Shape):
        """Register a shape with a given type."""
        ShapeFactory.shapes[shape_type.lower()] = shape_instance

    @staticmethod
    def create_shape(shape_type: str, *args) -> Shape:
        """Create a shape based on the provided type."""
        shape_type = shape_type.lower()
        if shape_type not in ShapeFactory.shapes:
            raise ValueError(f"Shape type '{shape_type}' is not registered.")
        return ShapeFactory.shapes[shape_type]

# Sample usage
if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=6)

    ShapeFactory.register_shape('circle', circle)
    ShapeFactory.register_shape('rectangle', rectangle)

    # Create shapes using the factory
    created_circle = ShapeFactory.create_shape('circle')
    created_rectangle = ShapeFactory.create_shape('rectangle')

    print(f'Circle Area: {created_circle.area()}')  # Expected: Circle Area: 78.53975
    print(f'Rectangle Area: {created_rectangle.area()}')  # Expected: Rectangle Area: 24