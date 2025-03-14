import json

class User:
    """
    A class to represent a user.
    """
    def __init__(self, username, email):
        """
        Initialize the user with a username and email.
        """
        self.username = username
        self.email = email

    def to_dict(self):
        """
        Convert the user to a dictionary format.
        """
        return {'username': self.username, 'email': self.email}

class UserManager:
    """
    A class to manage a collection of users.
    """
    def __init__(self):
        """
        Initialize the user manager with an empty user list.
        """
        self.users = []

    def add_user(self, user):
        """
        Add a user to the user list.
        """
        self.users.append(user)

    def save_to_file(self, filename):
        """
        Save the user list to a JSON file.
        """
        with open(filename, 'w') as f:
            json.dump([user.to_dict() for user in self.users], f)

    def load_from_file(self, filename):
        """
        Load users from a JSON file into the user list.
        """
        with open(filename, 'r') as f:
            user_data = json.load(f)
            for data in user_data:
                self.add_user(User(data['username'], data['email']))

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('johndoe', 'john@example.com'))
    manager.add_user(User('janedoe', 'jane@example.com'))
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(user.to_dict())