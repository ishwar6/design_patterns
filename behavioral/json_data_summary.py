import json
import os
from typing import List, Dict

class DataProcessor:
    """Processes JSON data files and generates summary statistics."""

    def __init__(self, directory: str) -> None:
        """Initializes the DataProcessor with a directory to scan for JSON files."""
        self.directory = directory

    def load_data(self) -> List[Dict]:
        """Loads all JSON files in the specified directory and returns their contents."""
        data = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    data.append(json.load(file))
        return data

    def summarize_data(self, data: List[Dict]) -> Dict:
        """Generates summary statistics from the loaded data."""
        total_entries = len(data)
        summary = {
            'total_entries': total_entries,
            'fields': set(),
            'examples': []
        }
        for entry in data:
            summary['fields'].update(entry.keys())
            if len(summary['examples']) < 5:
                summary['examples'].append(entry)
        summary['fields'] = list(summary['fields'])
        return summary

    def save_summary(self, summary: Dict, output_file: str) -> None:
        """Saves the summary statistics to a JSON file."""
        with open(output_file, 'w') as file:
            json.dump(summary, file, indent=4)

    def process(self, output_file: str) -> None:
        """Loads data, summarizes it, and saves the summary."""
        data = self.load_data()
        summary = self.summarize_data(data)
        self.save_summary(summary, output_file)

if __name__ == '__main__':
    processor = DataProcessor('data')
    processor.process('summary.json')
    print('Data processing complete, summary saved to summary.json')