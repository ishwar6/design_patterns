import json
from typing import List, Dict

class DataProcessor:
    """Processes and filters data based on specified criteria."""

    def __init__(self, data: List[Dict[str, str]]) -> None:
        """Initializes the DataProcessor with a list of data dictionaries."""
        self.data = data

    def filter_by_key(self, key: str, value: str) -> List[Dict[str, str]]:
        """Filters the data for entries matching the specified key-value pair."""
        return [entry for entry in self.data if entry.get(key) == value]

    def save_to_json(self, filtered_data: List[Dict[str, str]], filename: str) -> None:
        """Saves the filtered data to a JSON file."""
        with open(filename, 'w') as json_file:
            json.dump(filtered_data, json_file, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': '30', 'city': 'New York'},
        {'name': 'Bob', 'age': '25', 'city': 'Los Angeles'},
        {'name': 'Charlie', 'age': '30', 'city': 'Chicago'},
    ]
    processor = DataProcessor(sample_data)
    filtered = processor.filter_by_key('age', '30')
    processor.save_to_json(filtered, 'filtered_data.json')
    print(f'Filtered data saved: {filtered}')