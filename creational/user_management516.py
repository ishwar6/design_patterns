import json

class User:
    """Represents a user with a name and email."""
    def __init__(self, name, email):
        """Initializes a user with name and email."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts the user instance to a dictionary."""
        return {'name': self.name, 'email': self.email}

class UserManager:
    """Manages a collection of users."""
    def __init__(self):
        """Initializes an empty user manager."""
        self.users = []

    def add_user(self, user):
        """Adds a new user to the manager."""
        self.users.append(user)

    def save_to_file(self, filename):
        """Saves the users to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('Alice', 'alice@example.com'))
    manager.add_user(User('Bob', 'bob@example.com'))
    manager.save_to_file('users.json')
    print('Users saved to users.json')