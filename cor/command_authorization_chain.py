#lets take another example: 
# Involves creating a series of handlers, each responsible for verifying a level of authorization before a command is executed. 
# This pattern is particularly useful in systems where commands need to pass through multiple authorization checks, such as in security-sensitive applications.


from abc import ABC, abstractmethod

class AuthorizationHandler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    @abstractmethod
    def authorize(self, command):
        pass


# Concrete Handlers for Different Authorization Levels

class BasicAuthorizationHandler(AuthorizationHandler):
    def authorize(self, command):
      # I have defined user_has_basic_rights() in client class, it is part of that. 
        if command.user_has_basic_rights():
            print("Basic Authorization: Passed")
            if self.next_handler:
                self.next_handler.authorize(command)
        else:
            print("Basic Authorization: Failed")

class ManagerAuthorizationHandler(AuthorizationHandler):
    def authorize(self, command):
        if command.user_is_manager():
            print("Manager Authorization: Passed")
            if self.next_handler:
                self.next_handler.authorize(command)
        else:
            print("Manager Authorization: Failed")

class AdminAuthorizationHandler(AuthorizationHandler):
    def authorize(self, command):
        if command.user_is_admin():
            print("Admin Authorization: Passed")
            if self.next_handler:
                self.next_handler.authorize(command)
        else:
            print("Admin Authorization: Failed")


# Command Class: the client here

class Command:
    # Dummy user roles for demonstration
    def __init__(self, user_role):
        self.user_role = user_role

    def user_has_basic_rights(self):
        return self.user_role in ["basic", "manager", "admin"]

    def user_is_manager(self):
        return self.user_role in ["manager", "admin"]

    def user_is_admin(self):
        return self.user_role == "admin"


# Setting Up the Authorization Chain


class CommandExecutor:
    def __init__(self):
        self.basic_auth_handler = BasicAuthorizationHandler()
        self.manager_auth_handler = ManagerAuthorizationHandler()
        self.admin_auth_handler = AdminAuthorizationHandler()

        # Setting up the chain
        self.basic_auth_handler.set_next(self.manager_auth_handler)
        self.manager_auth_handler.set_next(self.admin_auth_handler)

    def execute(self, command):
        self.basic_auth_handler.authorize(command)


 # Client Code to Execute a Command

executor = CommandExecutor()
command = Command(user_role="manager")
executor.execute(command)

#output
Basic Authorization: Passed
Manager Authorization: Passed
Admin Authorization: Failed


