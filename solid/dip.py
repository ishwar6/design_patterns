# Dependency inversion principle
# Bookish (wiki): The principle states:

# High-level modules should not import anything from low-level modules. Both should depend on abstractions (e.g., interfaces).
# Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions.


#this class violates DIP:

class EmailService:
    def send_email(self, message):
        print(f"Sending Email: {message}")

class SMSService:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self):
        self.email_service = EmailService()
        self.sms_service = SMSService()

    def send_message(self, message, type):
        if type == "email":
            self.email_service.send_email(message)
        elif type == "sms":
            self.sms_service.send_sms(message)


#but how?? -> NotificationManager depends on concrete classes like EmailService and SMSService; 


# To follow DIP, we introduce abstractions (interfaces) for dependencies and invert the direction of the dependencies.


from abc import ABC, abstractmethod

class TheMessageService(ABC):
    @abstractmethod
    def send_message(self, message):
        pass

class EmailService(TheMessageService):
    def send_message(self, message):
        print(f"Sending Email: {message}")

class SMSService(TheMessageService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")

class NotificationManager:
    def __init__(self, message_service: TheMessageService):
        self.message_service = message_service

    def notify(self, message):
        self.message_service.send_message(message)



# NotificationManager depends on the TheMessageService interface, not specific implementations.
# It's easy to extend the system with new services (like push notifications) without modifying NotificationManager.
# The system is more flexible and adheres to the open-closed principle, as new functionalities can be added with minimal changes.


#  Let's make it little simple: 

# DIP is like making sure that both a family’s head (father) and a family member (son) follow the same family rules (abstractions)
# son do tasks but independenly and father dont poke his work. But Father keep an eye on each task. 
# rather than directly imposing responsibilities on each other. 

from abc import ABC, abstractmethod

# Abstraction (Family Rules, it tells how to do tasks)
class HouseholdChore(ABC):
    @abstractmethod
    def perform_task(self):
        pass



# High-Level Module (Father: don't directly engage in tasks)
class Father:
    def __init__(self, chore: HouseholdChore):
        self.chore = chore

    def manage_house(self):
        self.chore.perform_task()



# Low-Level Module (this tell how Son will do the task)
class GarbageDisposal(HouseholdChore):
    def perform_task(self):
        print("Son is taking out the trash.")

class DishWashing(HouseholdChore):
    def perform_task(self):
        print("Son is washing the dishes.")

# Usage
# a task:
garbage_disposal = GarbageDisposal()
father = Father(garbage_disposal)

# Father can use any of low level module: 

father.manage_house()  # Output: Son is taking out the trash.

# The father's management can easily switch to another chore without changing the son's method of performing it.
dish_washing = DishWashing()
father = Father(dish_washing)
father.manage_house()  # Output: Son is washing the dishes.








