# structural/geometry.py

from typing import List, Tuple, Optional

class GeometryError(Exception):
    """Custom exception for geometry related errors."""
    pass

class Rectangle:
    """A class representing a rectangle."""

    def __init__(self, width: float, height: float):
        if width <= 0 or height <= 0:
            raise GeometryError("Width and height must be positive values.")
        self.width = width
        self.height = height

    def area(self) -> float:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

def largest_rectangle(rectangles: List[Rectangle]) -> Optional[Rectangle]:
    """Find the largest rectangle by area from a list of rectangles."""
    if not rectangles:
        return None
    largest = max(rectangles, key=lambda r: r.area())
    return largest

def rectangles_summary(rectangles: List[Rectangle]) -> List[Tuple[float, float, float, float]]:
    """Generate a summary of rectangles with their area and perimeter."""
    return [(rect.width, rect.height, rect.area(), rect.perimeter()) for rect in rectangles]

# Sample Usage
if __name__ == "__main__":
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(2, 3)
    rect3 = Rectangle(6, 8)

    rectangles = [rect1, rect2, rect3]

    largest = largest_rectangle(rectangles)
    summary = rectangles_summary(rectangles)

    print(f"Largest Rectangle - Width: {largest.width}, Height: {largest.height}, Area: {largest.area()}, Perimeter: {largest.perimeter()}")
    print("Summary of all rectangles (Width, Height, Area, Perimeter):")
    for rect_data in summary:
        print(rect_data)