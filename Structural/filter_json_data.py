import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initialize DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        """Load data from the JSON input file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            data = json.load(file)
        return data

    def process_data(self, data):
        """Process the loaded data by filtering out entries with a value less than a threshold."""
        threshold = 10
        filtered_data = [entry for entry in data if entry.get('value', 0) >= threshold]
        return filtered_data

    def save_data(self, data):
        """Save the processed data to the JSON output file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self):
        """Execute the load, process, and save operations."""
        data = self.load_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.run()