import json

class User:
    """Represents a user with a name and email."""
    def __init__(self, name, email):
        """Initializes a new user with name and email."""
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
        """Adds a user to the collection."""
        self.users.append(user)

    def save_to_file(self, filename):
        """Saves users to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def load_from_file(self, filename):
        """Loads users from a JSON file."""
        with open(filename, 'r') as file:
            user_data = json.load(file)
            for data in user_data:
                user = User(data['name'], data['email'])
                self.add_user(user)

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('Alice Smith', 'alice@example.com'))
    manager.add_user(User('Bob Johnson', 'bob@example.com'))
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(f'User: {user.name}, Email: {user.email}')