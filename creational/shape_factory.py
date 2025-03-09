# creational/factory.py

class Shape:
    """Base class for different shapes."""
    
    def area(self):
        """Calculate the area of the shape."""
        raise NotImplementedError("This method should be overridden by subclasses.")


class Circle(Shape):
    """Class representing a circle."""
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * (self.radius ** 2)


class Rectangle(Shape):
    """Class representing a rectangle."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height


class ShapeFactory:
    """Factory class to create shape objects."""
    
    @staticmethod
    def create_shape(shape_type, *args):
        """Creates a shape object based on the provided shape type."""
        shape_type = shape_type.lower()
        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'rectangle':
            return Rectangle(*args)
        else:
            raise ValueError(f"Unknown shape type: '{shape_type}'")


def main():
    """Example usage of the ShapeFactory."""
    try:
        circle = ShapeFactory.create_shape('circle', 5)
        rectangle = ShapeFactory.create_shape('rectangle', 4, 6)

        print(f"Circle area: {circle.area()}")
        print(f"Rectangle area: {rectangle.area()}")

    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()