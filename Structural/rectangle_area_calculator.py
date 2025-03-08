# structural/rectangle_area.py

class Rectangle:
    """
    A class to represent a rectangle.

    Attributes:
    width : float
        The width of the rectangle.
    height : float
        The height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initializes the Rectangle with width and height.

        Parameters:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.

        Raises:
        ValueError: If width or height is not positive.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive numbers.")
        
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
    Main function for testing the Rectangle class.
    """
    try:
        rect1 = Rectangle(5.0, 3.0)
        print(f"Rectangle 1 - Width: {rect1.width}, Height: {rect1.height}, Area: {rect1.area()}")

        rect2 = Rectangle(7.5, 2.0)
        print(f"Rectangle 2 - Width: {rect2.width}, Height: {rect2.height}, Area: {rect2.area()}")

        # Uncommenting the line below will raise an exception
        # rect3 = Rectangle(-1.0, 4.0)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()