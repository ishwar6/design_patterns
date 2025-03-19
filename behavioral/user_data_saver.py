import json

class User:
    """
    A class representing a user with a name and age.
    """
    def __init__(self, name, age):
        """
        Initialize a new User instance.
        """
        self.name = name
        self.age = age

    def to_dict(self):
        """
        Convert the User instance to a dictionary.
        """
        return {'name': self.name, 'age': self.age}

def save_users_to_file(users, file_path):
    """
    Save a list of User instances to a JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump([user.to_dict() for user in users], file)

if __name__ == '__main__':
    users = [User('Alice', 30), User('Bob', 25), User('Charlie', 35)]
    save_users_to_file(users, 'users.json')
    print('Users saved to users.json')