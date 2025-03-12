import json
from typing import List, Dict

class DataProcessor:
    """
    A class to process and analyze data from JSON files.
    """
    def __init__(self, file_path: str):
        """
        Initializes the DataProcessor with a file path.
        """
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self) -> List[Dict]:
        """
        Loads data from the specified JSON file.
        Returns a list of dictionaries.
        """
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, key: str, value: str) -> List[Dict]:
        """
        Filters the loaded data based on a key-value pair.
        """
        return [item for item in self.data if item.get(key) == value]

    def save_filtered_data(self, filtered_data: List[Dict], output_path: str) -> None:
        """
        Saves the filtered data to a specified JSON file.
        """
        with open(output_path, 'w') as file:
            json.dump(filtered_data, file, indent=4)

    def summary_statistics(self) -> Dict[str, int]:
        """
        Generates summary statistics for the loaded data.
        Returns a dictionary with counts of unique values for each key.
        """
        statistics = {}
        for item in self.data:
            for key in item:
                if key not in statistics:
                    statistics[key] = set()
                statistics[key].add(item[key])
        return {key: len(value) for key, value in statistics.items()}

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    filtered = processor.filter_data('category', 'electronics')
    processor.save_filtered_data(filtered, 'filtered_data.json')
    stats = processor.summary_statistics()
    print(stats)