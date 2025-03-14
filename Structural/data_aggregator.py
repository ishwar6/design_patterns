import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initializes the DataProcessor with specified input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Reads data from the input JSON file and returns it as a dictionary."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the input data and returns aggregated results."""
        result = {"total": 0, "count": 0}
        for item in data:
            result["total"] += item.get("value", 0)
            result["count"] += 1
        result["average"] = result["total"] / result["count"] if result["count"] > 0 else 0
        return result

    def write_data(self, data):
        """Writes the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self):
        """Executes the data processing workflow: read, process, and write data."""
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)
        print(f"Processed data saved to {self.output_file}")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_data.json')
    processor.run()