import json
from typing import List, Dict

class User:
    """Represents a user with a name and age."""
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def to_dict(self) -> Dict[str, str]:
        """Converts the User object to a dictionary."""
        return {'name': self.name, 'age': self.age}

class UserManager:
    """Handles operations related to users."""
    def __init__(self):
        self.users: List[User] = []

    def add_user(self, user: User) -> None:
        """Adds a user to the user manager."""
        self.users.append(user)

    def save_users_to_file(self, filename: str) -> None:
        """Saves the list of users to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def load_users_from_file(self, filename: str) -> None:
        """Loads users from a JSON file into the user manager."""
        with open(filename, 'r') as file:
            users_data = json.load(file)
            self.users = [User(**data) for data in users_data]

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('Alice', 30))
    manager.add_user(User('Bob', 25))
    manager.save_users_to_file('users.json')
    manager.load_users_from_file('users.json')
    for user in manager.users:
        print(user.to_dict())