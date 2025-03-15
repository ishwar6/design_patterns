import json
import os

class DataProcessor:
    """
    A class to process and store JSON data.
    """

    def __init__(self, file_path):
        """
        Initializes the DataProcessor with a file path.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """
        Loads JSON data from the specified file.
        """
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r') as file:
                return json.load(file)
        return {}

    def save_data(self):
        """
        Saves the current data to the specified file.
        """
        with open(self.file_path, 'w') as file:
            json.dump(self.data, file, indent=4)

    def add_entry(self, key, value):
        """
        Adds a new entry to the data.
        """
        self.data[key] = value
        self.save_data()

    def get_entry(self, key):
        """
        Retrieves an entry from the data.
        """
        return self.data.get(key, None)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    processor.add_entry('name', 'John Doe')
    processor.add_entry('age', 30)
    print(processor.get_entry('name'))
    print(processor.get_entry('age'))