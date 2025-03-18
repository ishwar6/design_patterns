import json

class User:
    """
    Class representing a user.
    """
    def __init__(self, username, email):
        """
        Initializes a new user with a username and email.
        """
        self.username = username
        self.email = email

    def to_dict(self):
        """
        Converts the user object to a dictionary.
        """
        return {'username': self.username, 'email': self.email}

class UserManager:
    """
    Class to manage user operations.
    """
    def __init__(self):
        """
        Initializes an empty user list.
        """
        self.users = []

    def add_user(self, user):
        """
        Adds a user to the user list.
        """
        self.users.append(user)

    def save_users(self, file_path):
        """
        Saves the list of users to a JSON file.
        """
        with open(file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_users(self, file_path):
        """
        Loads users from a JSON file.
        """
        with open(file_path, 'r') as file:
            users_data = json.load(file)
            self.users = [User(data['username'], data['email']) for data in users_data]

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('john_doe', 'john@example.com'))
    manager.add_user(User('jane_smith', 'jane@example.com'))
    manager.save_users('users.json')
    print('Users saved to users.json')
    manager.load_users('users.json')
    print('Loaded users:', [user.to_dict() for user in manager.users])