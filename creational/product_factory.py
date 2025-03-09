# creational/factory_pattern.py

from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class representing a product."""
    
    @abstractmethod
    def operation(self) -> str:
        """Returns the operation provided by the product."""
        pass


class ConcreteProductA(Product):
    """Concrete implementation of Product A."""

    def operation(self) -> str:
        return "Operation of Product A."


class ConcreteProductB(Product):
    """Concrete implementation of Product B."""

    def operation(self) -> str:
        return "Operation of Product B."


class Creator(ABC):
    """Abstract base class for creators, declaring the factory method."""
    
    @abstractmethod
    def factory_method(self) -> Product:
        """Factory method to create a product."""
        pass

    def some_operation(self) -> str:
        """Performs some operation involving the product."""
        product = self.factory_method()
        return f"Creator: The same creator's code just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    """Concrete creator for Product A."""

    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """Concrete creator for Product B."""

    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    """Function that utilizes the creator and its products."""
    print(creator.some_operation())


if __name__ == "__main__":
    print("Client: I can work with different creators:\n")
    client_code(ConcreteCreatorA())
    print("\n")
    client_code(ConcreteCreatorB())