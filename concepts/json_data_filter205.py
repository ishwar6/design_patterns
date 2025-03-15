import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initialize the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Read data from the input JSON file and return it as a dictionary."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} not found.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Process the input data by filtering out entries without 'value' key."""
        return [entry for entry in data if 'value' in entry]

    def save_data(self, data):
        """Save the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def execute(self):
        """Run the data processing workflow: read, process, and save data."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)
        print(f"Processed {len(processed_data)} valid entries out of {len(data)} total.")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_data.json')
    processor.execute()