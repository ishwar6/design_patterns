import json
from datetime import datetime

class User:
    """
    Represents a user with a name and registration date.
    """
    def __init__(self, name):
        """
        Initializes a new user with a name and the current date.
        """
        self.name = name
        self.registration_date = datetime.now().isoformat()

    def to_dict(self):
        """
        Converts the user instance to a dictionary.
        """
        return {"name": self.name, "registration_date": self.registration_date}

class UserManager:
    """
    Manages a collection of users and handles saving to a JSON file.
    """
    def __init__(self, filename):
        """
        Initializes the user manager with a specific filename.
        """
        self.filename = filename
        self.users = []

    def add_user(self, user):
        """
        Adds a new user to the collection.
        """
        self.users.append(user)

    def save_to_file(self):
        """
        Saves the users to a JSON file.
        """
        with open(self.filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

if __name__ == '__main__':
    manager = UserManager('users.json')
    user1 = User('Alice')
    user2 = User('Bob')
    manager.add_user(user1)
    manager.add_user(user2)
    manager.save_to_file()
    print('Users saved to users.json')