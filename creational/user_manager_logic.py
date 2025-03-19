import json
from typing import List, Dict

class User:
    """Class representing a user with a name and age."""
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def to_dict(self) -> Dict[str, str]:
        """Convert user instance to dictionary representation."""
        return {'name': self.name, 'age': self.age}

class UserManager:
    """Class to manage multiple users and their data operations."""
    def __init__(self) -> None:
        self.users = []

    def add_user(self, user: User) -> None:
        """Add a user to the manager."""
        self.users.append(user)

    def to_json(self) -> str:
        """Convert all users to JSON format."""
        return json.dumps([user.to_dict() for user in self.users], indent=4)

    def save_to_file(self, file_path: str) -> None:
        """Save user data to a specified JSON file."""
        with open(file_path, 'w') as file:
            file.write(self.to_json())

if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.add_user(User('Alice', 30))
    user_manager.add_user(User('Bob', 25))
    user_manager.save_to_file('users.json')
    print('User data saved to users.json')