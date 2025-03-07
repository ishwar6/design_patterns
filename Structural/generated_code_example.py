python
class StructuralFeature:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def calculate(self):
        return self.value * 2

    def display(self):
        print(f"{self.name}: {self.value}")

    @staticmethod
    def static_method_example():
        return "This is a static method example."

if __name__ == "__main__":
    feature = StructuralFeature("ExampleFeature", 10)
    feature.display()
    print(f"Calculated value: {feature.calculate()}")
    print(StructuralFeature.static_method_example())