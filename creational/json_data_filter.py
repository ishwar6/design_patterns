import json
from typing import List, Dict

class DataProcessor:
    """Processes and analyzes JSON data from a file."""
    def __init__(self, file_path: str) -> None:
        """Initializes DataProcessor with the path to the JSON file."""
        self.file_path = file_path

    def load_data(self) -> List[Dict]:
        """Loads JSON data from the specified file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, data: List[Dict], key: str, value: str) -> List[Dict]:
        """Filters the data based on a specified key-value pair."""
        return [item for item in data if item.get(key) == value]

    def save_filtered_data(self, filtered_data: List[Dict], output_path: str) -> None:
        """Saves the filtered data to a specified output file as JSON."""
        with open(output_path, 'w') as file:
            json.dump(filtered_data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    raw_data = processor.load_data()
    filtered = processor.filter_data(raw_data, 'category', 'books')
    processor.save_filtered_data(filtered, 'filtered_data.json')
    print(f'Filtered data saved to filtered_data.json with {len(filtered)} entries.')