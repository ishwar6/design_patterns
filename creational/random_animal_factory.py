# creational/animal_factory.py

from abc import ABC, abstractmethod
from random import choice


class Animal(ABC):
    """Abstract base class for animals."""
    
    @abstractmethod
    def make_sound(self) -> str:
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """Dog class implementing Animal interface."""
    
    def make_sound(self) -> str:
        return "Woof!"


class Cat(Animal):
    """Cat class implementing Animal interface."""
    
    def make_sound(self) -> str:
        return "Meow!"


class AnimalFactory:
    """Factory to create instances of Animal."""
    
    ANIMAL_TYPES = [Dog, Cat]
    
    @classmethod
    def create_random_animal(cls) -> Animal:
        """Create a random animal instance from the available animal types."""
        animal_class = choice(cls.ANIMAL_TYPES)
        return animal_class()


def main():
    """Main function to demonstrate the animal factory."""
    for _ in range(5):
        animal = AnimalFactory.create_random_animal()
        print(f'Created a {animal.__class__.__name__} that says: {animal.make_sound()}')


if __name__ == "__main__":
    main()