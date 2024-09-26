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
    def process_payment(self, amount:float):
        pass




# now we will do concrete implmentation for Paypal
class Paypal(PaymentProcessor):
    def process_payment(self, amount:float):
        print(f"processing payment of {amount} by paypal")
        return super().process_payment(amount)


class Stripe(PaymentProcessor):
    def process_payment(self, amount: float):
        print(f"Processing payment by stripe of {amount}")
        return super().process_payment(amount)



# now lets make checkout class

# The Checkout class now depends on the PaymentProcessor interface
class Checkout:
    def __init__(self, payment_processor: PaymentProcessor) -> None:
        self.payment_processor = payment_processor
    

    def process_order(self, amount:float):
        self.payment_processor.process_payment(amount)