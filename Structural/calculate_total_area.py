# structural/calculate_area.py

from typing import Union

class Shape:
    """Abstract base class for different shapes."""
    
    def area(self) -> Union[int, float]:
        """Calculate the area of the shape. This method should be overridden."""
        raise NotImplementedError("Must override area method")
    

class Rectangle(Shape):
    """Class to represent a rectangle."""
    
    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        """Initialize a rectangle with width and height."""
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        self.width = width
        self.height = height
        
    def area(self) -> float:
        """Return the area of the rectangle."""
        return self.width * self.height


class Circle(Shape):
    """Class to represent a circle."""
    
    def __init__(self, radius: Union[int, float]) -> None:
        """Initialize a circle with radius."""
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
        
    def area(self) -> float:
        """Return the area of the circle."""
        from math import pi
        return pi * (self.radius ** 2)


def calculate_total_area(shapes: list) -> float:
    """Calculate the total area of a list of shapes."""
    total_area = 0
    for shape in shapes:
        if not isinstance(shape, Shape):
            raise TypeError("All elements in the list must be instances of Shape.")
        total_area += shape.area()
    return total_area


# Sample usage
if __name__ == "__main__":
    rectangle = Rectangle(3, 4)
    circle = Circle(5)
    shapes = [rectangle, circle]
    
    total_area = calculate_total_area(shapes)
    print(f"Total area of shapes: {total_area}")