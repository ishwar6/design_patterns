import json

class User:
    """Represents a user with a name and email."""
    def __init__(self, name, email):
        """Initializes the User with name and email."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts the User object to a dictionary."""
        return {'name': self.name, 'email': self.email}

class UserManager:
    """Manages a collection of Users."""
    def __init__(self):
        """Initializes an empty UserManager."""
        self.users = []

    def add_user(self, user):
        """Adds a User to the collection."""
        self.users.append(user)

    def save_to_file(self, file_path):
        """Saves the users to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def load_from_file(self, file_path):
        """Loads users from a JSON file."""
        with open(file_path, 'r') as file:
            user_data = json.load(file)
            for data in user_data:
                self.add_user(User(data['name'], data['email']))

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('Alice', 'alice@example.com'))
    manager.add_user(User('Bob', 'bob@example.com'))
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(f'User: {user.name}, Email: {user.email}')