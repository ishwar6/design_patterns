import json
import os

class DataProcessor:
    """
    A class to process and analyze JSON data files.
    """

    def __init__(self, directory):
        """
        Initializes the DataProcessor with a directory containing JSON files.
        """
        self.directory = directory

    def load_data(self, file_name):
        """
        Loads JSON data from a specified file.
        """
        file_path = os.path.join(self.directory, file_name)
        with open(file_path, 'r') as file:
            return json.load(file)

    def save_summary(self, summary, output_file):
        """
        Saves the summary data to a specified output file in JSON format.
        """
        with open(output_file, 'w') as file:
            json.dump(summary, file, indent=4)

    def analyze_data(self):
        """
        Analyzes all JSON files in the directory and generates a summary.
        """
        summary = {}
        for file_name in os.listdir(self.directory):
            if file_name.endswith('.json'):
                data = self.load_data(file_name)
                summary[file_name] = self.perform_analysis(data)
        self.save_summary(summary, 'summary_output.json')

    def perform_analysis(self, data):
        """
        Performs some analysis on the loaded data and returns the result.
        """
        total_entries = len(data)
        return {'total_entries': total_entries}

if __name__ == '__main__':
    processor = DataProcessor('./data')
    processor.analyze_data()