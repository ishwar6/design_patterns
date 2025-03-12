import json

class UserProfile:
    """Represents a user profile with basic information and methods to manage it."""
    def __init__(self, username, email):
        """Initializes the user profile with username and email."""
        self.username = username
        self.email = email
        self.preferences = {}

    def update_preferences(self, preferences):
        """Updates user preferences with a given dictionary."""
        self.preferences.update(preferences)

    def to_json(self):
        """Converts user profile to a JSON string for storage."""
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_string):
        """Creates a user profile from a JSON string."""
        data = json.loads(json_string)
        profile = cls(data['username'], data['email'])
        profile.preferences = data['preferences']
        return profile

if __name__ == '__main__':
    user = UserProfile('john_doe', 'john@example.com')
    user.update_preferences({'theme': 'dark', 'notifications': True})
    json_data = user.to_json()
    print('Serialized User Profile:', json_data)
    new_user = UserProfile.from_json(json_data)
    print('Deserialized User Profile:', new_user.__dict__)