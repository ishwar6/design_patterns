# structural/shape_area_calculator.py

from typing import Union, Dict

class ShapeAreaCalculator:
    """
    A class to calculate the area of various geometric shapes.
    Supported shapes: Circle, Rectangle, Triangle.
    """
    
    def calculate_area(self, shape: str, dimensions: Dict[str, Union[int, float]]) -> float:
        """
        Calculate the area for the given shape and its dimensions.
        
        :param shape: The type of shape ('circle', 'rectangle', 'triangle').
        :param dimensions: A dictionary containing the dimensions required to compute the area.
                           - For circle: {'radius': float}
                           - For rectangle: {'length': float, 'width': float}
                           - For triangle: {'base': float, 'height': float}
        :return: The area of the shape as a float.
        :raises ValueError: If the shape is unsupported or dimensions are invalid.
        """
        if shape.lower() == 'circle':
            return self._calculate_circle_area(dimensions.get('radius', 0))
        elif shape.lower() == 'rectangle':
            return self._calculate_rectangle_area(dimensions.get('length', 0), dimensions.get('width', 0))
        elif shape.lower() == 'triangle':
            return self._calculate_triangle_area(dimensions.get('base', 0), dimensions.get('height', 0))
        else:
            raise ValueError(f"Unsupported shape: {shape}. Please use 'circle', 'rectangle', or 'triangle'.")

    def _calculate_circle_area(self, radius: float) -> float:
        if radius < 0:
            raise ValueError("Radius cannot be negative.")
        return 3.14159 * radius ** 2

    def _calculate_rectangle_area(self, length: float, width: float) -> float:
        if length < 0 or width < 0:
            raise ValueError("Length and width cannot be negative.")
        return length * width

    def _calculate_triangle_area(self, base: float, height: float) -> float:
        if base < 0 or height < 0:
            raise ValueError("Base and height cannot be negative.")
        return 0.5 * base * height

# Sample Usage
if __name__ == "__main__":
    calculator = ShapeAreaCalculator()
    
    circle_area = calculator.calculate_area('circle', {'radius': 5})
    print(f"Circle area: {circle_area:.2f}")
    
    rectangle_area = calculator.calculate_area('rectangle', {'length': 4, 'width': 6})
    print(f"Rectangle area: {rectangle_area:.2f}")
    
    triangle_area = calculator.calculate_area('triangle', {'base': 3, 'height': 4})
    print(f"Triangle area: {triangle_area:.2f}")