import json

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def to_dict(self):
        return {'username': self.username, 'email': self.email}

class UserManager:
    def __init__(self):
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            user_data = json.load(file)
            self.users = [User(**data) for data in user_data]

if __name__ == '__main__':
    manager = UserManager()
    manager.add_user(User('john_doe', 'john@example.com'))
    manager.add_user(User('jane_smith', 'jane@example.com'))
    manager.save_to_file('users.json')
    manager.load_from_file('users.json')
    for user in manager.users:
        print(f'User: {user.username}, Email: {user.email}')