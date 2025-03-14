import json
from pathlib import Path

class DataProcessor:
    """
    A class to process and transform data from JSON files.
    """
    def __init__(self, input_file, output_file):
        """
        Initializes the DataProcessor with input and output file paths.
        """
        self.input_file = Path(input_file)
        self.output_file = Path(output_file)

    def load_data(self):
        """
        Loads data from the input JSON file.
        """
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def transform_data(self, data):
        """
        Transforms the data by filtering out entries with a specific condition.
        """
        return [entry for entry in data if entry.get('active')]

    def save_data(self, data):
        """
        Saves the transformed data to the output JSON file.
        """
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def process(self):
        """
        Executes the data loading, transforming, and saving process.
        """
        data = self.load_data()
        transformed_data = self.transform_data(data)
        self.save_data(transformed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.process()