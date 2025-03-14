import json
import os

class DataProcessor:
    def __init__(self, directory):
        """Initializes the DataProcessor with a directory to process files."""
        self.directory = directory

    def load_data(self, filename):
        """Loads data from a specified JSON file."""
        with open(os.path.join(self.directory, filename), 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Processes the loaded data and returns a summary."""
        summary = {
            'total_entries': len(data),
            'average_value': sum(item['value'] for item in data) / len(data) if data else 0
        }
        return summary

    def save_summary(self, summary, output_filename):
        """Saves the summary to a JSON file."""
        with open(os.path.join(self.directory, output_filename), 'w') as file:
            json.dump(summary, file, indent=4)

    def run(self, input_filename, output_filename):
        """Runs the data processing workflow from loading data to saving summary."""
        data = self.load_data(input_filename)
        summary = self.process_data(data)
        self.save_summary(summary, output_filename)
        print(f"Summary saved to {output_filename} with data: {summary}")

if __name__ == '__main__':
    processor = DataProcessor('./data')
    processor.run('input_data.json', 'summary_output.json')