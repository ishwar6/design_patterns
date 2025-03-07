python
class StructuralFeature:
    def __init__(self, name, material, dimensions):
        self.name = name
        self.material = material
        self.dimensions = dimensions

    def calculate_volume(self):
        length, width, height = self.dimensions
        return length * width * height

    def display_info(self):
        return {
            'Name': self.name,
            'Material': self.material,
            'Dimensions': self.dimensions,
            'Volume': self.calculate_volume()
        }

    def update_dimensions(self, new_dimensions):
        self.dimensions = new_dimensions