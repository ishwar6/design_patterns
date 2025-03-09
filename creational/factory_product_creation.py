# creational/factory_pattern.py

from typing import Protocol, TypeVar, List

T = TypeVar('T')

class Product(Protocol):
    """Protocol for products created by the factory."""
    
    def operation(self) -> str:
        """Perform an operation and return result as string."""
        ...

class ConcreteProductA:
    """A concrete product that implements the Product interface."""
    
    def operation(self) -> str:
        return "Result of ConcreteProductA"

class ConcreteProductB:
    """Another concrete product that implements the Product interface."""
    
    def operation(self) -> str:
        return "Result of ConcreteProductB"

class Creator(Protocol):
    """Protocol for creators that will create different products."""
    
    def factory_method(self) -> Product:
        """The factory method that should return a new Product."""
        ...

class ConcreteCreatorA:
    """A concrete creator that generates ConcreteProductA."""
    
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB:
    """A concrete creator that generates ConcreteProductB."""
    
    def factory_method(self) -> Product:
        return ConcreteProductB()

def client_code(creator: Creator) -> str:
    """Function to demonstrate the use of the creator and product."""
    product = creator.factory_method()
    return product.operation()

def create_products(creators: List[Creator]) -> List[str]:
    """Create products using a list of creators and return their operations."""
    results = []
    for creator in creators:
        results.append(client_code(creator))
    return results

if __name__ == "__main__":
    creators = [ConcreteCreatorA(), ConcreteCreatorB()]
    results = create_products(creators)
    
    for result in results:
        print(result)