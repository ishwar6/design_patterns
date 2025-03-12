import json

class User:
    """
    A class to represent a user.
    """
    def __init__(self, username, email):
        """
        Initialize a new user with username and email.
        """
        self.username = username
        self.email = email

    def to_dict(self):
        """
        Convert user instance to dictionary.
        """
        return {'username': self.username, 'email': self.email}

class UserManager:
    """
    A class to manage a collection of users.
    """
    def __init__(self):
        """
        Initialize an empty user manager.
        """
        self.users = []

    def add_user(self, user):
        """
        Add a user to the user manager.
        """
        self.users.append(user)

    def save_to_file(self, filename):
        """
        Save the users to a JSON file.
        """
        with open(filename, 'w') as f:
            json.dump([user.to_dict() for user in self.users], f, indent=4)

    def load_from_file(self, filename):
        """
        Load users from a JSON file.
        """
        with open(filename, 'r') as f:
            users_data = json.load(f)
            self.users = [User(data['username'], data['email']) for data in users_data]

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('john_doe', 'john@example.com'))
    manager.add_user(User('jane_smith', 'jane@example.com'))
    manager.save_to_file('users.json')
    print('Users saved to users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(f'Loaded user: {user.username}, Email: {user.email}')