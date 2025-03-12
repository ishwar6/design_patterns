import json

class User:
    def __init__(self, username, email):
        """Initialize a new user with a username and email."""
        self.username = username
        self.email = email

    def to_dict(self):
        """Convert user instance to dictionary representation."""
        return {'username': self.username, 'email': self.email}

def save_users_to_file(users, filename):
    """Save a list of User instances to a JSON file."""
    with open(filename, 'w') as file:
        json.dump([user.to_dict() for user in users], file, indent=4)

if __name__ == '__main__':
    users = [User('john_doe', 'john@example.com'), User('jane_doe', 'jane@example.com')]
    save_users_to_file(users, 'users.json')
    print('Users saved to users.json')