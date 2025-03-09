# structural/geometry_calculator.py

class GeometryCalculator:
    """A class to perform geometric calculations for various shapes."""

    @staticmethod
    def calculate_circle_area(radius: float) -> float:
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
        return 3.14159 * radius ** 2

    @staticmethod
    def calculate_rectangle_area(length: float, width: float) -> float:
        """Calculate the area of a rectangle given its length and width.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.

        Returns:
            float: The area of the rectangle.

        Raises:
            ValueError: If either length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        return length * width

    @staticmethod
    def calculate_triangle_area(base: float, height: float) -> float:
        """Calculate the area of a triangle given its base and height.

        Args:
            base (float): The base of the triangle.
            height (float): The height of the triangle.

        Returns:
            float: The area of the triangle.

        Raises:
            ValueError: If either base or height is negative.
        """
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height


def main():
    """Demonstrates the usage of the GeometryCalculator."""
    try:
        circle_area = GeometryCalculator.calculate_circle_area(5)
        rectangle_area = GeometryCalculator.calculate_rectangle_area(4, 6)
        triangle_area = GeometryCalculator.calculate_triangle_area(3, 7)

        print(f"Circle area (radius 5): {circle_area:.2f}")
        print(f"Rectangle area (length 4, width 6): {rectangle_area:.2f}")
        print(f"Triangle area (base 3, height 7): {triangle_area:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()