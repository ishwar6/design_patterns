# structural_analysis.py

class StructuralElement:
    """
    A class to represent a structural element.

    Attributes:
        name (str): The name of the structural element.
        length (float): The length of the structural element in meters.
        area (float): The cross-sectional area of the element in square meters.
        youngs_modulus (float): The Young's modulus of the material in Pascals.
    """

    def __init__(self, name: str, length: float, area: float, youngs_modulus: float):
        self.name = name
        self.length = length
        self.area = area
        self.youngs_modulus = youngs_modulus

    def calculate_stress(self, force: float) -> float:
        """
        Calculate the stress on the structural element.

        Args:
            force (float): The applied force in Newtons.

        Returns:
            float: Calculated stress in Pascals.
        """
        if self.area <= 0:
            raise ValueError("Area must be greater than zero.")
        return force / self.area

    def calculate_strain(self, force: float) -> float:
        """
        Calculate the strain on the structural element using Hooke's Law.

        Args:
            force (float): The applied force in Newtons.

        Returns:
            float: Calculated strain (dimensionless).
        """
        stress = self.calculate_stress(force)
        if self.youngs_modulus <= 0:
            raise ValueError("Young's modulus must be greater than zero.")
        return stress / self.youngs_modulus

    def calculate_deflection(self, force: float) -> float:
        """
        Calculate the deflection at the midpoint of a simply supported beam.

        Args:
            force (float): The applied force in Newtons.

        Returns:
            float: Calculated deflection in meters.
        """
        if self.length <= 0:
            raise ValueError("Length must be greater than zero.")
        # Assuming the load is applied at the midpoint.
        return (force * self.length**3) / (48 * self.youngs_modulus * self.area * self.length)

def main():
    element = StructuralElement(name="Beam A", length=5.0, area=0.1, youngs_modulus=200e9)
    
    force = 10000  # Applied force in Newtons
    stress = element.calculate_stress(force)
    strain = element.calculate_strain(force)
    deflection = element.calculate_deflection(force)

    print(f"{element.name} Analysis Results:")
    print(f"Applied Force: {force} N")
    print(f"Calculated Stress: {stress:.2f} Pa")
    print(f"Calculated Strain: {strain:.5f}")
    print(f"Calculated Deflection: {deflection:.5f} m")

if __name__ == "__main__":
    main()