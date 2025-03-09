# creational/factory.py

from typing import Protocol, TypeVar, Any

T = TypeVar('T')

class Product(Protocol):
    def operation(self) -> str:
        """Return a string describing the operation of the product."""

class ConcreteProductA:
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB:
    def operation(self) -> str:
        return "Result of ConcreteProductB"

class Creator:
    @staticmethod
    def factory_method(product_type: str) -> Product:
        """Factory method to create products based on type."""
        if product_type == "A":
            return ConcreteProductA()
        elif product_type == "B":
            return ConcreteProductB()
        else:
            raise ValueError(f"Unknown product type: {product_type}")

def use_product(product: Product) -> None:
    """Use the product and print its operation result."""
    print(product.operation())

if __name__ == "__main__":
    product_a = Creator.factory_method("A")
    use_product(product_a)

    product_b = Creator.factory_method("B")
    use_product(product_b)

    try:
        invalid_product = Creator.factory_method("C")
        use_product(invalid_product)
    except ValueError as e:
        print(e)