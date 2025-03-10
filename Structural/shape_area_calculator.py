# structural/shape_calculator.py

import math
from typing import Union, Tuple

class ShapeCalculator:
    """A class that provides calculations for various geometric shapes."""

    @staticmethod
    def area_circle(radius: float) -> float:
        """Calculate the area of a circle given its radius.
        
        Args:
            radius (float): The radius of the circle.
        
        Returns:
            float: The area of the circle.
        
        Raises:
            ValueError: If the radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return math.pi * (radius ** 2)

    @staticmethod
    def area_rectangle(width: float, height: float) -> float:
        """Calculate the area of a rectangle given its width and height.
        
        Args:
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.
        
        Returns:
            float: The area of the rectangle.
        
        Raises:
            ValueError: If width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height cannot be negative.")
        return width * height

    @staticmethod
    def area_triangle(base: float, height: float) -> float:
        """Calculate the area of a triangle given its base and height.
        
        Args:
            base (float): The base of the triangle.
            height (float): The height of the triangle.
        
        Returns:
            float: The area of the triangle.
        
        Raises:
            ValueError: If base or height is negative.
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height

def calculate_shape_areas(shapes: list) -> list:
    """Calculate areas for a list of shape specifications.
    
    Args:
        shapes (list): A list of tuples where each tuple specifies a shape
                       and its dimensions in the form (shape_type, dimensions).
                       shape_type can be 'circle', 'rectangle', or 'triangle'.
                       dimensions is a tuple of the necessary dimensions.
                       
    Returns:
        list: A list of calculated areas, or errors if any invalid values were provided.
    """
    results = []
    for shape in shapes:
        shape_type, dimensions = shape[0], shape[1:]
        try:
            if shape_type == 'circle':
                results.append(ShapeCalculator.area_circle(*dimensions))
            elif shape_type == 'rectangle':
                results.append(ShapeCalculator.area_rectangle(*dimensions))
            elif shape_type == 'triangle':
                results.append(ShapeCalculator.area_triangle(*dimensions))
            else:
                results.append(f"Unknown shape type: {shape_type}")
        except ValueError as e:
            results.append(str(e))
    return results

# Sample usage
if __name__ == "__main__":
    shapes_to_calculate = [
        ('circle', 5),
        ('rectangle', 3, 4),
        ('triangle', 6, 7),
        ('circle', -1),  # This will raise an error
        ('unknown_shape', 5)
    ]
    
    areas = calculate_shape_areas(shapes_to_calculate)
    for shape, area in zip(shapes_to_calculate, areas):
        print(f"Shape: {shape[0]}, Dimensions: {shape[1:]}, Area: {area}")