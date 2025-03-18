import json
from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict]) -> None:
        """Initializes the DataProcessor with a list of dictionaries."""
        self.data = data

    def filter_by_key(self, key: str, value: str) -> List[Dict]:
        """Filters the data by a specific key and value."""
        return [item for item in self.data if item.get(key) == value]

    def calculate_average(self, key: str) -> float:
        """Calculates the average of numeric values associated with a specific key."""
        total = sum(item.get(key, 0) for item in self.data if isinstance(item.get(key), (int, float)))
        count = sum(1 for item in self.data if isinstance(item.get(key), (int, float)))
        return total / count if count > 0 else 0.0

    def to_json(self, output_file: str) -> None:
        """Writes the data to a JSON file."""
        with open(output_file, 'w') as f:
            json.dump(self.data, f, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'score': 85},
        {'name': 'Bob', 'age': 22, 'score': 90},
        {'name': 'Charlie', 'age': 30, 'score': 95},
        {'name': 'David', 'age': 22, 'score': 80}
    ]
    processor = DataProcessor(sample_data)
    filtered_data = processor.filter_by_key('age', '30')
    print('Filtered Data:', filtered_data)
    average_score = processor.calculate_average('score')
    print('Average Score:', average_score)
    processor.to_json('output.json')
    print('Data written to output.json')