import json

class User:
    """
    Represents a user with a name and email.
    """
    def __init__(self, name, email):
        """
        Initializes the User with name and email.
        """
        self.name = name
        self.email = email

    def to_dict(self):
        """
        Converts User instance to a dictionary.
        """
        return {'name': self.name, 'email': self.email}

class UserManager:
    """
    Manages a collection of users, allowing for addition and export to JSON.
    """
    def __init__(self):
        """
        Initializes the UserManager with an empty user list.
        """
        self.users = []

    def add_user(self, user):
        """
        Adds a User instance to the user list.
        """
        self.users.append(user)

    def export_to_json(self, file_path):
        """
        Exports the user list to a JSON file.
        """
        with open(file_path, 'w') as f:
            json.dump([user.to_dict() for user in self.users], f)

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user(User('Alice Smith', 'alice@example.com'))
    user_manager.add_user(User('Bob Johnson', 'bob@example.com'))
    user_manager.export_to_json('users.json')
    print('Users exported to users.json')