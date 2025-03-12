import json
import os

class DataProcessor:
    """Processes JSON data for analysis and reporting."""
    def __init__(self, input_file, output_file):
        """Initializes the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Reads JSON data from the input file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the input data by filtering and transforming it."""
        return [entry for entry in data if entry.get('active')]

    def write_data(self, data):
        """Writes the processed data to the output file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def execute(self):
        """Executes the data processing workflow."""
        raw_data = self.read_data()
        processed_data = self.process_data(raw_data)
        self.write_data(processed_data)
        print(f"Processed data written to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.execute()