import json
from typing import Dict, List

class DataProcessor:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize the DataProcessor with a list of dictionaries."""
        self.data = data

    def filter_data(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filter data based on a given key and value."""
        return [item for item in self.data if item.get(key) == value]

    def to_json(self, filtered_data: List[Dict[str, str]], output_file: str) -> None:
        """Save filtered data to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(filtered_data, f, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'city': 'New York'},
        {'name': 'Bob', 'city': 'Los Angeles'},
        {'name': 'Charlie', 'city': 'New York'},
    ]
    processor = DataProcessor(sample_data)
    filtered = processor.filter_data('city', 'New York')
    processor.to_json(filtered, 'filtered_data.json')
    print('Filtered data saved to filtered_data.json')