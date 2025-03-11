import json
import os

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

class UserManager:
    def __init__(self, storage_file):
        self.storage_file = storage_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, 'r') as file:
            return [User(**data) for data in json.load(file)]

    def save_users(self):
        with open(self.storage_file, 'w') as file:
            json.dump([{'username': user.username, 'email': user.email} for user in self.users], file)

    def add_user(self, username, email):
        new_user = User(username, email)
        self.users.append(new_user)
        self.save_users()
        print(f'User {username} added.')

    def list_users(self):
        for user in self.users:
            print(f'Username: {user.username}, Email: {user.email}')

if __name__ == '__main__':
    user_manager = UserManager('users.json')
    user_manager.add_user('john_doe', 'john@example.com')
    user_manager.list_users()