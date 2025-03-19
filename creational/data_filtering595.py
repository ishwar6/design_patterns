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
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Process the data to filter out entries with age less than 18."""
        return [entry for entry in data if entry.get('age', 0) >= 18]

    def write_data(self, processed_data):
        """Write processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(processed_data, file, indent=4)

    def execute(self):
        """Run the data processing pipeline: read, process, and write data."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
        print(f"Processed data written to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_data.json')
    processor.execute()