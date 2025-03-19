import json
from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict]):
        """Initialize with a list of dictionaries."""
        self.data = data

    def filter_by_key(self, key: str, value: str) -> List[Dict]:
        """Filter data by a specific key-value pair."""
        return [item for item in self.data if item.get(key) == value]

    def to_json(self, filtered_data: List[Dict], output_file: str) -> None:
        """Write filtered data to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(filtered_data, f, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'city': 'New York'},
        {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': 30, 'city': 'Chicago'}
    ]
    processor = DataProcessor(sample_data)
    filtered = processor.filter_by_key('age', '30')
    processor.to_json(filtered, 'output.json')
    print(f'Filtered data saved to output.json: {filtered}')