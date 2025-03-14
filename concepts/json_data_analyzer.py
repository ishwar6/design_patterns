import json
import os

class DataProcessor:
    """Class for processing and analyzing JSON data files."""

    def __init__(self, directory):
        """Initialize DataProcessor with a directory to scan for JSON files."""
        self.directory = directory

    def load_json_files(self):
        """Load all JSON files in the specified directory and return their contents."""
        data = []
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    data.append(json.load(file))
        return data

    def analyze_data(self, data):
        """Analyze loaded data to calculate summary statistics."""
        summary = {
            'total_files': len(data),
            'total_entries': sum(len(d) for d in data),
            'average_entries_per_file': sum(len(d) for d in data) / len(data) if data else 0
        }
        return summary

    def save_summary(self, summary, output_file):
        """Save the summary statistics to a JSON file."""
        with open(output_file, 'w') as file:
            json.dump(summary, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data')
    json_data = processor.load_json_files()
    summary_stats = processor.analyze_data(json_data)
    processor.save_summary(summary_stats, 'summary.json')
    print('Summary statistics saved to summary.json')