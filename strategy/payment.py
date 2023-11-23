#We need to design a payment processing system for a company that can easily adapt to different payment methods without requiring significant changes to the core system 
#each time a new method is introduced.

# The Strategy Design Pattern is ideal for this scenario. 
# It allows the payment processing system to dynamically select the appropriate payment strategy based on the customer’s choice, making the system highly flexible and maintainable.

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
    
    
class CreditCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing Rs {amount} via Credit card"
        
class DebitCardPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing Rs {amount}  via Debit card"

class CryptoPayment(PaymentStrategy):
    def process_payment(self, amount):
        return f"Processing Rs {amount}  via Crypto"
        
        
#context class: or client class that will use

class PaymentProcessor:
    def __init__(self, strategy: PaymentStrategy):
        self.strategy = strategy
        
    def set_payment_method(self, strategy):
        self.strategy = strategy
        
    def execute_payment(self, amount):
        return self.strategy.process_payment(amount)
        
        
        
#caller class
credit_card_payment_obj = CreditCardPayment()
#we will plug this class in our client: 

processor = PaymentProcessor(credit_card_payment_obj)
print(processor.execute_payment(100))


crypto_payment_obj = CryptoPayment()

#we will plug this class in our client: 

processor = PaymentProcessor(crypto_payment_obj)
print(processor.execute_payment(10))

# output: 
# Processing Rs 100 via Credit card
# Processing Rs 10  via Crypto

    
