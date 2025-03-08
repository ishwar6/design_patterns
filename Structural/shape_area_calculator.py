# structural/shape_area_calculator.py

class ShapeAreaCalculator:
    """A calculator for the areas of various geometric shapes."""

    @staticmethod
    def calculate_circle_area(radius: float) -> float:
        """Calculate the area of a circle given its radius.

        Args:
            radius (float): The radius of the circle.

        Returns:
            float: The area of the circle.

        Raises:
            ValueError: If radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return 3.14159 * (radius ** 2)

    @staticmethod
    def calculate_rectangle_area(width: float, height: float) -> float:
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
    def calculate_triangle_area(base: float, height: float) -> float:
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


if __name__ == "__main__":
    # Sample usage
    try:
        circle_area = ShapeAreaCalculator.calculate_circle_area(5)
        print(f"Circle Area (radius=5): {circle_area:.2f}")

        rectangle_area = ShapeAreaCalculator.calculate_rectangle_area(4, 3)
        print(f"Rectangle Area (width=4, height=3): {rectangle_area:.2f}")

        triangle_area = ShapeAreaCalculator.calculate_triangle_area(6, 2)
        print(f"Triangle Area (base=6, height=2): {triangle_area:.2f}")

    except ValueError as e:
        print(e)