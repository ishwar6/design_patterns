# structural/geometry.py

from typing import List, Tuple

class Polygon:
    """Class to represent a polygon and calculate its properties."""

    def __init__(self, vertices: List[Tuple[float, float]]):
        """
        Initializes the Polygon with a list of vertices.

        Args:
            vertices (List[Tuple[float, float]]): A list of tuples representing the vertices 
                                                   of the polygon in (x, y) format.
        """
        if len(vertices) < 3:
            raise ValueError("A polygon must have at least 3 vertices.")
        self.vertices = vertices

    def area(self) -> float:
        """Calculates the area of the polygon using the Shoelace formula.

        Returns:
            float: The area of the polygon.
        """
        n = len(self.vertices)
        area = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2.0
    
    def perimeter(self) -> float:
        """Calculates the perimeter of the polygon.

        Returns:
            float: The perimeter of the polygon.
        """
        n = len(self.vertices)
        perimeter = 0.0
        for i in range(n):
            x1, y1 = self.vertices[i]
            x2, y2 = self.vertices[(i + 1) % n]
            distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
            perimeter += distance
        return perimeter

def main():
    """Demonstrates the usage of the Polygon class."""
    try:
        polygon = Polygon(vertices=[(0, 0), (4, 0), (4, 3), (0, 4)])
        print(f"Vertices: {polygon.vertices}")
        print(f"Area: {polygon.area()}")        # Outputs: Area: 12.0
        print(f"Perimeter: {polygon.perimeter()}")  # Outputs: Perimeter: 14.0
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()