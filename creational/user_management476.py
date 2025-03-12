import json
from typing import List, Dict

class User:
    """Represents a user in the system."""
    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email

    def to_dict(self) -> Dict[str, str]:
        """Converts User instance to dictionary format."""
        return {'username': self.username, 'email': self.email}

class UserManager:
    """Handles operations related to users."""
    def __init__(self) -> None:
        self.users: List[User] = []

    def add_user(self, username: str, email: str) -> None:
        """Adds a new user to the manager."""
        user = User(username, email)
        self.users.append(user)

    def save_to_file(self, file_path: str) -> None:
        """Saves the list of users to a JSON file."""
        with open(file_path, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_from_file(self, file_path: str) -> None:
        """Loads users from a JSON file into the manager."""
        try:
            with open(file_path, 'r') as file:
                user_data = json.load(file)
                self.users = [User(**data) for data in user_data]
        except FileNotFoundError:
            print("File not found. Starting with an empty user list.")

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user('john_doe', 'john@example.com')
    manager.add_user('jane_doe', 'jane@example.com')
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(user.to_dict())