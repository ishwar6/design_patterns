import json
from typing import List, Dict

class DataProcessor:
    def __init__(self, data: List[Dict[str, int]]) -> None:
        """Initializes the DataProcessor with a list of data dictionaries."""
        self.data = data

    def filter_data(self, threshold: int) -> List[Dict[str, int]]:
        """Filters the data based on a threshold value."""
        return [item for item in self.data if item['value'] > threshold]

    def calculate_average(self, filtered_data: List[Dict[str, int]]) -> float:
        """Calculates the average value from the filtered data."""
        total = sum(item['value'] for item in filtered_data)
        return total / len(filtered_data) if filtered_data else 0.0

    def process_data(self, threshold: int) -> Dict[str, float]:
        """Processes the data by filtering and calculating the average."""
        filtered = self.filter_data(threshold)
        average = self.calculate_average(filtered)
        return {'filtered_data': filtered, 'average': average}

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 5},
        {'id': 4, 'value': 30}
    ]
    processor = DataProcessor(sample_data)
    result = processor.process_data(15)
    print(json.dumps(result, indent=2))