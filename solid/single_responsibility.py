# Code that is not following Single Responsibility Principle


class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    def save_user(self):
        # Save user to the database
        print(f"User {self.name} saved to the database.")

    def send_email(self, content):
        # Send an email to the user
        print(f"Email sent to {self.email} with content: {content}")


# Issues in this Code:
# The User class has two reasons to change: changes in how users are saved to the database and changes in how emails are sent.
# If the email sending mechanism changes (like using a different email service), we have to modify the User class, which is not related to the user entity itself.

# LETS REFACTOR
# Definition:
# The Single Responsibility Principle, one of the five SOLID principles of object-oriented design, states that 
#a class should have only one reason to change. -> This means that a class should only have one job or responsibility.

# Benefits:
# Easier to Understand and Maintain: Classes with a single responsibility are generally smaller and clearer.
# Reduced Coupling: Changes in one part of the system have minimal impact on other parts.
# Improved Testability: Testing is easier when each class has a single responsibility.

# Violation of SRP:
# When a class is handling more than one responsibility, it becomes complex, harder to understand, and more prone to bugs. 
#Changes in one responsibility may affect the other, violating the principle as we saw in above case. 



class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

class UserRepository:
    def save(self, user: User):
        # Save user to the database
        print(f"User {user.name} saved to the database.")

class EmailService:
    def send_email(self, user: User, content: str):
        # Send an email to the user
        print(f"Email sent to {user.email} with content: {content}")



# User Class: Now solely responsible for representing a user.
# UserRepository Class: Handles all data persistence logic related to users.
# EmailService Class: Manages the email sending functionality.

new_user = User("Ishwar", "iisudrj11@gmail.com")
user_repo = UserRepository()
user_repo.save(new_user)

# Send an email to the user
email_service = EmailService()
email_service.send_email(new_user, "Welcome to our service!")

# OUTPUT:
# User Ishwar saved to the database.
# Email sent to iisudrj11@gmail.com with content: Welcome to our service!




