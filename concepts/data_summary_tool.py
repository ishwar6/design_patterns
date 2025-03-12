import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initializes DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Reads data from the input JSON file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"{self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the data to calculate the total and average values."""
        total = sum(data)
        average = total / len(data) if data else 0
        return {'total': total, 'average': average}

    def write_data(self, results):
        """Writes the processed results to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(results, file, indent=4)

    def execute(self):
        """Executes the data processing workflow."""
        data = self.read_data()
        results = self.process_data(data)
        self.write_data(results)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.execute()
    print(f'Processed data saved to {processor.output_file}')