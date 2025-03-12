import json
from typing import List, Dict

class DataProcessor:
    """Class to process and store data from JSON files."""

    def __init__(self, file_path: str) -> None:
        """Initialize DataProcessor with a file path."""
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict]:
        """Load data from a JSON file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, key: str, value: str) -> List[Dict]:
        """Filter data by a key-value pair."""
        return [item for item in self.data if item.get(key) == value]

    def save_filtered_data(self, filtered_data: List[Dict], output_file: str) -> None:
        """Save filtered data to a new JSON file."""
        with open(output_file, 'w') as file:
            json.dump(filtered_data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    filtered = processor.filter_data('status', 'active')
    processor.save_filtered_data(filtered, 'filtered_data.json')
    print(f'Filtered data saved to filtered_data.json with {len(filtered)} entries.')