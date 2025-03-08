# file: concepts/calculator.py

class Calculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, a: float, b: float) -> float:
        """Return the sum of two numbers."""
        return a + b

    def subtract(self, a: float, b: float) -> float:
        """Return the difference of two numbers."""
        return a - b

    def multiply(self, a: float, b: float) -> float:
        """Return the product of two numbers."""
        return a * b

    def divide(self, a: float, b: float) -> float:
        """Return the quotient of two numbers. Raises ZeroDivisionError if b is zero."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

def main():
    """Demonstrate the usage of the Calculator class."""
    calc = Calculator()
    
    try:
        print("Addition: 5 + 3 =", calc.add(5, 3))
        print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
        print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
        print("Division: 5 / 3 =", calc.divide(5, 3))
        print("Division by zero: 5 / 0 =", calc.divide(5, 0))
    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()