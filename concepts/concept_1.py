# "Program to an interface, not an implementation"

"""
Instead of depending directly on concrete implementations (specific classes), 
you should depend on abstractions (interfaces or abstract classes). 
This allows your code to be less tightly coupled to specific implementations, 
making it easier to modify, extend, or swap out implementations without changing the client code that depends on them.
"""


# Bad Approach (Program to an Implementation)

class PaymentProvider:
    def process_payment(self, amount):
        paypal = Paypal()
        paypal.checkout()
        paypal.success()


"""
A bad approach would be to hard-code everything 
for each payment provider inside the logic itself, which would make it difficult to switch providers later.
"""

# Better Approach (Program to an Interface):

from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    
    @abstractmethod
    def process_payment(self, amount):
        pass

