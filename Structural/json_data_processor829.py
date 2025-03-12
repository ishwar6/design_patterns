import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initializes the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        """Loads data from the input JSON file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the loaded data by filtering out entries without 'value' key."""
        return [item for item in data if 'value' in item]

    def save_data(self, data):
        """Saves the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self):
        """Executes the data processing workflow: load, process, and save data."""
        data = self.load_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_data.json')
    processor.run()