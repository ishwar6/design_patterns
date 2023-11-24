# a software entity (like a class, module, or function) should be open for extension but closed for modification. 
# This means that the behavior of the entity can be extended without altering its source code.


#without following OCP: 

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

# The ReportGenerator class has to be modified every time we need to add support for a new report type.
# This frequent modification increases the risk of introducing bugs into our existing code.


#with OCP

class User:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

#these are our Concrete Report Classes: one way one class one report (Modi Style)
class UserRepository:
    def save(self, user: User):
        # Save user to the database
        print(f"User {user.name} saved to the database.")

class EmailService:
    def send_email(self, user: User, content: str):
        # Send an email to the user
        print(f"Email sent to {user.email} with content: {content}")



def main():
    # Create a new user
    new_user = User("Ishwar", "ishwarjdev@gmail.com)

    # Save the user to the database
    user_repo = UserRepository()
    user_repo.save(new_user)

    # Send an email to the user
    email_service = EmailService()
    email_service.send_email(new_user, "Welcome to my design pattern github!")

if __name__ == "__main__":
    main()


# Report Class: An abstract base class Report is defined with an abstract method generate.
# Concrete Report Classes: PDFReport and ExcelReport extend Report and implement the generate method.
# ReportGenerator Class: It no longer needs to change. It can work with any subclass of Report.
