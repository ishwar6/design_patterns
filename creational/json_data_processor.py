import json
from typing import List, Dict

class DataProcessor:
    """Processes and transforms data from JSON files."""

    def __init__(self, input_file: str, output_file: str) -> None:
        """Initializes DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self) -> List[Dict]:
        """Reads JSON data from the input file."""
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def transform_data(self, data: List[Dict]) -> List[Dict]:
        """Transforms the data by filtering and modifying entries."""
        return [
            {"name": item['name'], "age": item['age'] + 1}
            for item in data
            if item['age'] >= 18
        ]

    def write_data(self, data: List[Dict]) -> None:
        """Writes the transformed data to the output file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def process(self) -> None:
        """Executes the data processing workflow: read, transform, and write data."""
        data = self.read_data()
        transformed_data = self.transform_data(data)
        self.write_data(transformed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.process()