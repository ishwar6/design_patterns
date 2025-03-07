python
class StructuralFeature:
    def __init__(self, name, dimensions):
        self.name = name
        self.dimensions = dimensions

    def calculate_volume(self):
        if self.name == "Cube":
            return self.dimensions['side'] ** 3
        elif self.name == "Cylinder":
            return 3.14159 * (self.dimensions['radius'] ** 2) * self.dimensions['height']
        elif self.name == "Sphere":
            return (4/3) * 3.14159 * (self.dimensions['radius'] ** 3)
        else:
            raise ValueError("Unknown shape")

    def display_info(self):
        return f"{self.name} with dimensions {self.dimensions} has a volume of {self.calculate_volume()}"