import json

class User:
    """Represents a user in the system."""
    def __init__(self, username, email):
        """Initializes a new user with a username and email."""
        self.username = username
        self.email = email

    def to_dict(self):
        """Converts the user object to a dictionary."""
        return {'username': self.username, 'email': self.email}

class UserManager:
    """Manages user operations such as creation and storage."""
    def __init__(self):
        """Initializes the user manager with an empty user list."""
        self.users = []

    def add_user(self, user):
        """Adds a user to the user list."""
        self.users.append(user)

    def save_to_file(self, file_path):
        """Saves the list of users to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user(User('john_doe', 'john@example.com'))
    user_manager.add_user(User('jane_smith', 'jane@example.com'))
    user_manager.save_to_file('users.json')
    print('User data saved to users.json')