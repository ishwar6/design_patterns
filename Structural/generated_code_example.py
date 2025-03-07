python
class StructuralFeature:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def calculate_area(self):
        if self.name == "Rectangle":
            return self.properties['length'] * self.properties['width']
        elif self.name == "Circle":
            import math
            return math.pi * (self.properties['radius'] ** 2)
        elif self.name == "Triangle":
            return 0.5 * self.properties['base'] * self.properties['height']
        else:
            raise ValueError("Unsupported shape")

    def display_info(self):
        return f"{self.name} with properties: {self.properties}"