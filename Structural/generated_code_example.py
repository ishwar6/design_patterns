python
class StructuralFeature:
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties

    def calculate_area(self):
        if self.properties['type'] == 'rectangle':
            return self.properties['width'] * self.properties['height']
        elif self.properties['type'] == 'circle':
            import math
            return math.pi * (self.properties['radius'] ** 2)
        else:
            raise ValueError("Unknown structural type")

    def display_info(self):
        area = self.calculate_area()
        return f"Structural Feature: {self.name}, Area: {area}"