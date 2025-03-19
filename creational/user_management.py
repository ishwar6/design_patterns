import json
from typing import List, Dict

class User:
    def __init__(self, name: str, age: int):
        """Initialize a User with a name and age."""
        self.name = name
        self.age = age

    def to_dict(self) -> Dict[str, str]:
        """Convert User instance to dictionary format."""
        return {'name': self.name, 'age': self.age}

class UserManager:
    def __init__(self):
        """Initialize UserManager with an empty user list."""
        self.users: List[User] = []

    def add_user(self, user: User):
        """Add a User instance to the user list."""
        self.users.append(user)

    def save_to_file(self, filename: str):
        """Save users to a JSON file."""
        with open(filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def load_from_file(self, filename: str):
        """Load users from a JSON file."""
        with open(filename, 'r') as file:
            users_data = json.load(file)
            for user_data in users_data:
                self.add_user(User(user_data['name'], user_data['age']))

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('Alice', 30))
    manager.add_user(User('Bob', 25))
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(f'User: {user.name}, Age: {user.age}')