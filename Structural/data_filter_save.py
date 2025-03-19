import json
from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initialize with a list of dictionaries containing data."""
        self.data = data

    def filter_by_key(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filter data by a specified key-value pair."""
        return [item for item in self.data if item.get(key) == value]

    def save_to_json(self, filtered_data: List[Dict[str, str]], filename: str) -> None:
        """Save the filtered data to a JSON file."""
        with open(filename, 'w') as json_file:
            json.dump(filtered_data, json_file, indent=4)

    def process_data(self, key: str, value: str, output_file: str) -> None:
        """Process the data: filter by key and save to a file."""
        filtered_data = self.filter_by_key(key, value)
        self.save_to_json(filtered_data, output_file)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': '30', 'city': 'New York'},
        {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': '30', 'city': 'Chicago'}
    ]
    processor = DataProcessor(sample_data)
    processor.process_data('age', '30', 'filtered_data.json')
    print('Data processing complete, output saved to filtered_data.json.')