#in COR: we have different handlers; they pass control to each other
#https://refactoring.guru/design-patterns/chain-of-responsibility

# Chain of Responsibility is a behavioral design pattern that lets you pass requests along a chain of handlers. 
# Upon receiving a request, each handler decides either to process the request or to pass it to the next handler in the chain.

from abc import ABC, abstractmethod


class ATMHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def dispense(self, amount):
        pass


#lets make class for each note
class Denomination2000Handler(ATMHandler):
    def dispense(self, amount):
        if amount >= 2000:
            num, remainder = divmod(amount, 2000)
            print(f"Dispensing {num} note(s) of Rs 2000")
            if remainder != 0:
                self.next_handler.dispense(remainder)
        else:
            self.next_handler.dispense(amount)

class Denomination500Handler(ATMHandler):
    def dispense(self, amount):
        if amount >= 500:
            num, remainder = divmod(amount, 500)
            print(f"Dispensing {num} note(s) of Rs 500")
            if remainder != 0:
                self.next_handler.dispense(remainder)
        else:
            self.next_handler.dispense(amount)

class Denomination100Handler(ATMHandler):
    def dispense(self, amount):
        if amount >= 100:
            num, remainder = divmod(amount, 100)
            print(f"Dispensing {num} note(s) of Rs 100")
            if remainder != 0:
                print(f"Cannot dispense Rs {remainder}! Amount should be in multiples of Rs 100.")
        else:
            print(f"Cannot dispense Rs {amount}! Amount should be in multiples of Rs 100.")


#the client class that will use above handlers
class ATM:
    def __init__(self):
        # Initialize handlers and set the chain
        self.handler2000 = Denomination2000Handler()
        self.handler500 = Denomination500Handler()
        self.handler100 = Denomination100Handler()

        #this is chain setup
        self.handler2000.set_next(self.handler500)
        self.handler500.set_next(self.handler100)

    def withdraw(self, amount):
        self.handler2000.dispense(amount)
        
        
#lets try the ATM

atm = ATM()
amount_to_withdraw = 3600
atm.withdraw(amount_to_withdraw)

