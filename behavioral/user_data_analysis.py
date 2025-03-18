import json
from typing import List, Dict

class DataProcessor:
    """
    A class to process JSON data for user analytics.
    """

    def __init__(self, data: List[Dict[str, str]]) -> None:
        """
        Initializes the DataProcessor with a list of user data.
        """
        self.data = data

    def filter_active_users(self) -> List[Dict[str, str]]:
        """
        Filters the list of users to include only active users.
        """
        return [user for user in self.data if user.get('active') == 'true']

    def calculate_average_age(self) -> float:
        """
        Calculates the average age of the users.
        """
        total_age = sum(int(user['age']) for user in self.data if 'age' in user)
        count = sum(1 for user in self.data if 'age' in user)
        return total_age / count if count > 0 else 0.0

    def save_filtered_data(self, filename: str) -> None:
        """
        Saves the filtered active users to a JSON file.
        """
        active_users = self.filter_active_users()
        with open(filename, 'w') as outfile:
            json.dump(active_users, outfile, indent=4)

if __name__ == '__main__':
    users_data = [
        {'name': 'Alice', 'age': '30', 'active': 'true'},
        {'name': 'Bob', 'age': '24', 'active': 'false'},
        {'name': 'Charlie', 'age': '28', 'active': 'true'},
        {'name': 'David', 'age': '35', 'active': 'true'},
    ]
    processor = DataProcessor(users_data)
    print('Average Age:', processor.calculate_average_age())
    processor.save_filtered_data('active_users.json')