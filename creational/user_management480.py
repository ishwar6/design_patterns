import json
from typing import List

class User:
    """Represents a user with a name and email."""
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email

class UserManager:
    """Manages a collection of users."""
    def __init__(self) -> None:
        self.users: List[User] = []

    def add_user(self, name: str, email: str) -> None:
        """Adds a new user to the collection."""
        self.users.append(User(name, email))

    def to_json(self) -> str:
        """Converts the user collection to a JSON string."""
        return json.dumps([{'name': user.name, 'email': user.email} for user in self.users])

    def save_to_file(self, filename: str) -> None:
        """Saves the user collection to a file in JSON format."""
        with open(filename, 'w') as file:
            file.write(self.to_json())

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user('Alice', 'alice@example.com')
    manager.add_user('Bob', 'bob@example.com')
    manager.save_to_file('users.json')
    print(f'Users saved to users.json: {manager.to_json()}')