import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initialize DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Read data from the input JSON file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} not found.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Process the input data and return the transformed data."""
        return {key: value * 2 for key, value in data.items() if isinstance(value, (int, float))}

    def save_data(self, data):
        """Save the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def execute(self):
        """Run the data processing workflow."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)
        print(f"Processed data saved to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.execute()