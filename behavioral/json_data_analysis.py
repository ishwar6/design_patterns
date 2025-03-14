import json
import os

class DataProcessor:
    """Class to process and analyze JSON data from files."""
    def __init__(self, directory):
        """Initializes the DataProcessor with a directory."""
        self.directory = directory
        self.data = []

    def load_data(self):
        """Loads JSON data from all files in the specified directory."""
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    self.data.append(json.load(file))

    def analyze_data(self):
        """Analyzes the loaded data and returns a summary."""
        summary = {}  
        for record in self.data:
            for key, value in record.items():
                if key not in summary:
                    summary[key] = []
                summary[key].append(value)
        return summary

    def save_summary(self, summary, output_file):
        """Saves the summary report to a JSON file."""
        with open(output_file, 'w') as file:
            json.dump(summary, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data')
    processor.load_data()
    summary = processor.analyze_data()
    processor.save_summary(summary, 'summary_report.json')
    print('Summary report generated successfully.')