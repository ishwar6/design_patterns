import json
import os
from typing import List, Dict

class DataProcessor:
    def __init__(self, input_file: str, output_file: str):
        """Initializes the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self) -> List[Dict]:
        """Loads data from the JSON input file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} not found.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data: List[Dict]) -> List[Dict]:
        """Processes the loaded data by filtering and transforming it."""
        return [
            {"name": item["name"], "value": item["value"] * 2}
            for item in data
            if item.get("value") is not None and item["value"] > 0
        ]

    def save_data(self, data: List[Dict]) -> None:
        """Saves the processed data to the output JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self) -> None:
        """Executes the data processing pipeline."""
        data = self.load_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)
        print(f"Processed data saved to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_data.json')
    processor.run()