import json
import os

class FileProcessor:
    """
    A class to process JSON files containing user data.
    """

    def __init__(self, directory):
        """
        Initializes the FileProcessor with a directory.
        :param directory: Path to the directory containing JSON files.
        """
        self.directory = directory

    def load_json_files(self):
        """
        Loads JSON files from the specified directory.
        :return: A list of dictionaries containing user data.
        """
        data = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    data.append(json.load(file))
        return data

    def filter_users_by_age(self, users, age_threshold):
        """
        Filters users based on age threshold.
        :param users: List of user dictionaries.
        :param age_threshold: Age to filter users.
        :return: Filtered list of users older than age_threshold.
        """
        return [user for user in users if user.get('age', 0) > age_threshold]

    def save_filtered_users(self, filtered_users, output_file):
        """
        Saves the filtered users to a JSON file.
        :param filtered_users: List of filtered user dictionaries.
        :param output_file: Output file path.
        """
        with open(output_file, 'w') as file:
            json.dump(filtered_users, file, indent=4)

if __name__ == '__main__':
    processor = FileProcessor('./data')
    users = processor.load_json_files()
    filtered_users = processor.filter_users_by_age(users, 30)
    processor.save_filtered_users(filtered_users, './output/filtered_users.json')
    print(f'Filtered users saved to ./output/filtered_users.json')