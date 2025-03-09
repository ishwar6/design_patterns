# structural/rectangle_area.py

class Rectangle:
    """
    Represents a rectangle in a 2D space.
    
    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the Rectangle with width and height.

        Args:
            width (float): The width of the rectangle. Must be non-negative.
            height (float): The height of the rectangle. Must be non-negative.
        
        Raises:
            ValueError: If width or height is negative.
        """
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.width * self.height


def main():
    """
    Demonstrates the usage of the Rectangle class by creating a rectangle 
    and calculating its area.
    """
    try:
        rectangle = Rectangle(5.0, 3.0)
        print(f"Width: {rectangle.width}, Height: {rectangle.height}")
        print(f"Area: {rectangle.area()}")  # Expected output: 15.0
        
        # Demonstrating edge case
        rectangle_negative = Rectangle(-1.0, 3.0)  # This will raise ValueError
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()