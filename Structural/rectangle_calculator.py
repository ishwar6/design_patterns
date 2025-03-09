# structural/geometry.py

from math import isclose

class Geometry:
    """
    A class representing a collection of geometric calculations.
    """

    @staticmethod
    def area_of_rectangle(length: float, width: float) -> float:
        """
        Calculate the area of a rectangle.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
        Returns:
        float: The area of the rectangle.
        
        Raises:
        ValueError: If length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        return length * width

    @staticmethod
    def perimeter_of_rectangle(length: float, width: float) -> float:
        """
        Calculate the perimeter of a rectangle.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
        Returns:
        float: The perimeter of the rectangle.
        
        Raises:
        ValueError: If length or width is negative.
        """
        if length < 0 or width < 0:
            raise ValueError("Length and width must be non-negative.")
        return 2 * (length + width)
    
    @staticmethod
    def is_square(length: float, width: float) -> bool:
        """
        Determine if a rectangle is also a square.
        
        Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
        
        Returns:
        bool: True if the rectangle is a square, otherwise False.
        """
        return isclose(length, width)

# Sample Usage Section
if __name__ == "__main__":
    try:
        length = 5.0
        width = 3.0
        
        area = Geometry.area_of_rectangle(length, width)
        perimeter = Geometry.perimeter_of_rectangle(length, width)
        square_check = Geometry.is_square(length, width)
        
        print(f"Area of rectangle: {area}")             # Output: Area of rectangle: 15.0
        print(f"Perimeter of rectangle: {perimeter}")   # Output: Perimeter of rectangle: 16.0
        print(f"Is the rectangle a square?: {square_check}")  # Output: Is the rectangle a square?: False
        
    except ValueError as e:
        print(e)