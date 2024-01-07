#Polymorphism vs Abstraction

# Python Code for Abstraction:

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def control_system(self):
        pass


# any car Sedan or SUV can use it. Or even electric. As far as they know how to implement it. -> this is abstraction. 

# This is Abstraction - focusing on the high-level mechanism for vehicle control without worrying about the specifics of each vehicle.


# Python code for polymorphism: 

class Sedan(Vehicle):
    def control_system(self):
        print("Standard Control System for Sedan")

class Truck(Vehicle):
    def control_system(self):
        print("Heavy-Duty Control System for Truck")

class ElectricCar(Vehicle):
    def control_system(self):
        print("Energy-Efficient Control System for Electric Car")

# Each class (Sedan, Truck, ElectricCar) has its own implementation of the control_system method.


#Using Abstraction and Polymorphism Together:

vehicles = [Sedan(), Truck(), ElectricCar()]

for vehicle in vehicles:
    vehicle.control_system()


# Abstraction is like creating a blueprint. It focuses on the high-level design, hiding the complex details. 
# It's about defining an interface or abstract concept.

# Polymorphism is like using the blueprint in different ways.
# It allows objects of different types to be treated as objects of a common super type, mainly through the use of inheritance and interfaces.


# Hence in summary: abstraction allowed us to define a general vehicle control system, while polymorphism make us implement system differently for each type of vehicle

