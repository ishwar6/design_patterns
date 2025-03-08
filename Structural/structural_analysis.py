class StructuralAnalyzer:
    def __init__(self, material_properties):
        self.material_properties = material_properties

    def calculate_stress(self, force, area):
        if area <= 0:
            raise ValueError("Area must be greater than zero.")
        return force / area

    def calculate_deflection(self, load, length, modulus_of_elasticity, moment_of_inertia):
        if moment_of_inertia <= 0:
            raise ValueError("Moment of inertia must be greater than zero.")
        return (load * length**3) / (3 * modulus_of_elasticity * moment_of_inertia)

    def check_safety(self, max_stress, allowable_stress):
        return max_stress <= allowable_stress

def main():
    material = {
        'modulus_of_elasticity': 200e9,
        'allowable_stress': 250e6,
        'moment_of_inertia': 5e-6
    }

    analyzer = StructuralAnalyzer(material)
    
    force = 10000
    area = 0.02
    length = 5

    stress = analyzer.calculate_stress(force, area)
    deflection = analyzer.calculate_deflection(force, length, material['modulus_of_elasticity'], material['moment_of_inertia'])
    safety_check = analyzer.check_safety(stress, material['allowable_stress'])

    results = {
        'stress': stress,
        'deflection': deflection,
        'is_safe': safety_check
    }

    return results

if __name__ == "__main__":
    output = main()
    print(output)