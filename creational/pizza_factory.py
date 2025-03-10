# creational/pizza_factory.py

from abc import ABC, abstractmethod

class Pizza(ABC):
    """Abstract base class for creating different types of pizza."""
    
    @abstractmethod
    def prepare(self):
        """Prepare the pizza."""
        pass

    @abstractmethod
    def bake(self):
        """Bake the pizza."""
        pass

    @abstractmethod
    def cut(self):
        """Cut the pizza."""
        pass

    @abstractmethod
    def box(self):
        """Box the pizza."""
        pass

class CheesePizza(Pizza):
    """Concrete implementation of a Cheese Pizza."""

    def prepare(self):
        return "Preparing Cheese Pizza with cheese and sauce."

    def bake(self):
        return "Baking Cheese Pizza at 450 degrees."

    def cut(self):
        return "Cutting Cheese Pizza into slices."

    def box(self):
        return "Boxing Cheese Pizza in a pizza box."

class VeggiePizza(Pizza):
    """Concrete implementation of a Veggie Pizza."""

    def prepare(self):
        return "Preparing Veggie Pizza with vegetables and sauce."

    def bake(self):
        return "Baking Veggie Pizza at 425 degrees."

    def cut(self):
        return "Cutting Veggie Pizza into slices."

    def box(self):
        return "Boxing Veggie Pizza in a pizza box."

class PizzaFactory:
    """Factory class to create pizza objects based on type."""

    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        """Create a pizza based on the provided type."""
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "veggie":
            return VeggiePizza()
        else:
            raise ValueError(f"Unknown pizza type: {pizza_type}")

def main():
    """Sample usage of the PizzaFactory."""
    pizza_types = ["cheese", "veggie"]
    for pizza_type in pizza_types:
        try:
            pizza = PizzaFactory.create_pizza(pizza_type)
            print(pizza.prepare())
            print(pizza.bake())
            print(pizza.cut())
            print(pizza.box())
            print()
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()