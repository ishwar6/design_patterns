import json
import os

class DataProcessor:
    """
    A class to process and manage JSON data files.
    """

    def __init__(self, directory):
        """
        Initializes the DataProcessor with a directory.
        """
        self.directory = directory

    def load_data(self, filename):
        """
        Loads data from a JSON file.
        """
        file_path = os.path.join(self.directory, filename)
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_data(self, filename, data):
        """
        Saves data to a JSON file.
        """
        file_path = os.path.join(self.directory, filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def filter_data(self, data, key, value):
        """
        Filters the data by a specific key-value pair.
        """
        return [item for item in data if item.get(key) == value]

    def process(self, input_file, output_file, key, value):
        """
        Loads, filters, and saves data based on given criteria.
        """
        data = self.load_data(input_file)
        filtered_data = self.filter_data(data, key, value)
        self.save_data(output_file, filtered_data)
        print(f'Processed data saved to {output_file}.')

if __name__ == '__main__':
    processor = DataProcessor('./data')
    processor.process('input.json', 'output.json', 'status', 'active')