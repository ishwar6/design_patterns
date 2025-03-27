import json
import os

class DataProcessor:
    """
    A class to process JSON data files.
    """

    def __init__(self, directory):
        """
        Initializes the DataProcessor with a directory.
        """
        self.directory = directory

    def load_data(self, filename):
        """
        Loads JSON data from a specified file.
        """
        file_path = os.path.join(self.directory, filename)
        with open(file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, data, key, threshold):
        """
        Filters data based on a key and threshold value.
        """
        return [item for item in data if item.get(key, 0) > threshold]

    def save_data(self, data, filename):
        """
        Saves the processed data to a specified file.
        """
        file_path = os.path.join(self.directory, filename)
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

    def process(self, input_file, output_file, key, threshold):
        """
        Main method to process the data: load, filter, and save it.
        """
        raw_data = self.load_data(input_file)
        filtered_data = self.filter_data(raw_data, key, threshold)
        self.save_data(filtered_data, output_file)

if __name__ == '__main__':
    processor = DataProcessor('data')
    processor.process('input.json', 'output.json', 'age', 30)
    print('Data processing complete. Filtered data saved to output.json.')