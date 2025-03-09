# creational/factory_method.py

from abc import ABC, abstractmethod

class Shape(ABC):
    """
    Abstract base class for shapes.
    """

    @abstractmethod
    def draw(self) -> None:
        """
        Draws the shape. Must be implemented by subclasses.
        """
        pass

class Circle(Shape):
    """
    Represents a circle shape.
    """

    def draw(self) -> None:
        """
        Draws a circle.
        """
        print("Drawing a Circle")

class Square(Shape):
    """
    Represents a square shape.
    """

    def draw(self) -> None:
        """
        Draws a square.
        """
        print("Drawing a Square")

class ShapeFactory:
    """
    Factory to create shapes.
    """

    @staticmethod
    def create_shape(shape_type: str) -> Shape:
        """
        Creates a shape based on the provided type.

        :param shape_type: The type of shape to create ('circle' or 'square').
        :returns: An instance of a shape.
        :raises ValueError: If an unsupported shape type is provided.
        """
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle()
        elif shape_type == 'square':
            return Square()
        else:
            raise ValueError(f"Unsupported shape type: {shape_type}")

# Sample usage
if __name__ == "__main__":
    try:
        shapes = ['circle', 'square', 'triangle']
        for shape_name in shapes:
            shape = ShapeFactory.create_shape(shape_name)
            shape.draw()
    except ValueError as e:
        print(e)