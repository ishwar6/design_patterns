# creational/factory_pattern.py

from typing import Dict, Type

class Shape:
    """Base class representing a generic shape."""
    def area(self) -> float:
        """Calculate the area of the shape."""
        pass


class Circle(Shape):
    """Class representing a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        """Calculate the area of the circle."""
        return 3.14159 * (self.radius ** 2)


class Rectangle(Shape):
    """Class representing a rectangle."""
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height


class ShapeFactory:
    """Factory class to create different shape instances."""
    _shapes: Dict[str, Type[Shape]] = {}

    @classmethod
    def register_shape(cls, shape_name: str, shape_class: Type[Shape]) -> None:
        """Register a shape class with a name."""
        cls._shapes[shape_name] = shape_class

    @classmethod
    def create_shape(cls, shape_name: str, *args, **kwargs) -> Shape:
        """Create a shape instance based on the given name."""
        shape_class = cls._shapes.get(shape_name)
        if not shape_class:
            raise ValueError(f"Shape '{shape_name}' is not registered.")
        return shape_class(*args, **kwargs)


# Sample usage of the factory pattern
if __name__ == "__main__":
    ShapeFactory.register_shape('circle', Circle)
    ShapeFactory.register_shape('rectangle', Rectangle)

    circle = ShapeFactory.create_shape('circle', radius=5)
    print(f"Circle area: {circle.area()}")  # Output: Circle area: 78.53975

    rectangle = ShapeFactory.create_shape('rectangle', width=4, height=6)
    print(f"Rectangle area: {rectangle.area()}")  # Output: Rectangle area: 24