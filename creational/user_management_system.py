import json

class User:
    """Represents a user with a name and email."""
    def __init__(self, name, email):
        """Initializes the User with a name and email."""
        self.name = name
        self.email = email

    def to_dict(self):
        """Converts User object to dictionary format for JSON serialization."""
        return {'name': self.name, 'email': self.email}

class UserManager:
    """Manages a collection of users."""
    def __init__(self):
        """Initializes an empty list of users."""
        self.users = []

    def add_user(self, user):
        """Adds a User object to the users list."""
        self.users.append(user)

    def save_to_file(self, file_path):
        """Saves the users list to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_from_file(self, file_path):
        """Loads users from a JSON file into the users list."""
        with open(file_path, 'r') as file:
            user_data = json.load(file)
            for item in user_data:
                self.add_user(User(item['name'], item['email']))

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user(User('Alice', 'alice@example.com'))
    user_manager.add_user(User('Bob', 'bob@example.com'))
    user_manager.save_to_file('users.json')
    user_manager.load_from_file('users.json')
    for user in user_manager.users:
        print(f'User: {user.name}, Email: {user.email}')