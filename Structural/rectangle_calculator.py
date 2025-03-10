# structural/rectangle.py

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    -----------
    length : float
        Length of the rectangle.
    width : float
        Width of the rectangle.
    
    Methods:
    --------
    area() -> float:
        Calculates and returns the area of the rectangle.
    
    perimeter() -> float:
        Calculates and returns the perimeter of the rectangle.
    
    is_square() -> bool:
        Checks if the rectangle is a square.
    """

    def __init__(self, length: float, width: float):
        """
        Initializes a Rectangle instance with specified length and width.

        Parameters:
        -----------
        length : float
            Length of the rectangle.
        width : float
            Width of the rectangle.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Length and width must be positive values.")
        self.length = length
        self.width = width

    def area(self) -> float:
        """
        Calculates the area of the rectangle.

        Returns:
        --------
        float
            The area of the rectangle.
        """
        return self.length * self.width

    def perimeter(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        Returns:
        --------
        float
            The perimeter of the rectangle.
        """
        return 2 * (self.length + self.width)

    def is_square(self) -> bool:
        """
        Checks if the rectangle is a square.

        Returns:
        --------
        bool
            True if the rectangle is a square, otherwise False.
        """
        return self.length == self.width


# Sample Usage
if __name__ == "__main__":
    try:
        rect = Rectangle(5, 10)
        print(f"Area: {rect.area()}")           # Output: Area: 50
        print(f"Perimeter: {rect.perimeter()}") # Output: Perimeter: 30
        print(f"Is square: {rect.is_square()}") # Output: Is square: False

        square = Rectangle(4, 4)
        print(f"Area: {square.area()}")         # Output: Area: 16
        print(f"Is square: {square.is_square()}") # Output: Is square: True
    except ValueError as e:
        print(e)