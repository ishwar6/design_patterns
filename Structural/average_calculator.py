import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initialize DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Read JSON data from the input file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        with open(self.input_file, 'r') as file:
            data = json.load(file)
        return data

    def process_data(self, data):
        """Process the input data to calculate average values."""
        processed_data = {}
        for key, values in data.items():
            if isinstance(values, list) and values:
                processed_data[key] = sum(values) / len(values)
        return processed_data

    def write_data(self, processed_data):
        """Write processed data to the output file in JSON format."""
        with open(self.output_file, 'w') as file:
            json.dump(processed_data, file, indent=4)

    def run(self):
        """Execute the data processing flow."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.run()