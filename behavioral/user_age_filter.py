import json
import os

class DataProcessor:
    """Handles data processing tasks for user interactions."""
    def __init__(self, input_file, output_file):
        """Initializes the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Reads data from the input JSON file and returns it as a dictionary."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} not found.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the input data by filtering users older than a specified age."""
        return [user for user in data if user.get('age', 0) > 18]

    def save_data(self, processed_data):
        """Saves the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(processed_data, file, indent=4)

    def run(self):
        """Executes the data processing workflow: reading, processing, and saving data."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)
        print(f"Processed data saved to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.run()