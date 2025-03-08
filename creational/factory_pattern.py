# creational/factory_pattern.py

from abc import ABC, abstractmethod


class Product(ABC):
    """Abstract base class representing a product."""
    
    @abstractmethod
    def operation(self) -> str:
        """Method to be implemented by concrete products."""
        pass


class ConcreteProductA(Product):
    """Concrete implementation of Product A."""
    
    def operation(self) -> str:
        return "Result of ConcreteProductA"


class ConcreteProductB(Product):
    """Concrete implementation of Product B."""
    
    def operation(self) -> str:
        return "Result of ConcreteProductB"


class Creator(ABC):
    """Abstract base class for creators."""
    
    @abstractmethod
    def factory_method(self) -> Product:
        """Factory method to be overridden by subclasses."""
        pass

    def some_operation(self) -> str:
        """Function that utilizes the product."""
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    """Concrete creator that produces ConcreteProductA."""
    
    def factory_method(self) -> Product:
        return ConcreteProductA()


class ConcreteCreatorB(Creator):
    """Concrete creator that produces ConcreteProductB."""
    
    def factory_method(self) -> Product:
        return ConcreteProductB()


def client_code(creator: Creator) -> None:
    """Function that takes a creator and uses it."""
    print(creator.some_operation())


if __name__ == "__main__":
    print("Client: Creating product A.")
    client_code(ConcreteCreatorA())
    
    print("\nClient: Creating product B.")
    client_code(ConcreteCreatorB())