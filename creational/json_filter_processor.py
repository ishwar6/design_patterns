import json
from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize with a list of dictionaries."""
        self.data = data

    def filter_by_key(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filter the data by a specific key-value pair."""
        return [item for item in self.data if item.get(key) == value]

    def to_json(self, filtered_data: List[Dict[str, str]], output_file: str) -> None:
        """Save filtered data to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(filtered_data, f, indent=4)

    def process_data(self, key: str, value: str, output_file: str) -> None:
        """Process the data by filtering and saving to a file."""
        filtered_data = self.filter_by_key(key, value)
        self.to_json(filtered_data, output_file)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York'},
        {'name': 'Bob', 'city': 'Los Angeles'},
        {'name': 'Charlie', 'city': 'New York'},
    ]
    processor = DataProcessor(sample_data)
    processor.process_data('city', 'New York', 'filtered_data.json')
    print('Data processed and saved to filtered_data.json')