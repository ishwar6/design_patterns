import json
import os

class DataProcessor:
    """
    A class to process and save data from a JSON file.
    """
    def __init__(self, input_file, output_file):
        """
        Initializes the DataProcessor with input and output file paths.
        """
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        """
        Loads data from the input JSON file.
        Returns a list of dictionaries.
        """
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file '{self.input_file}' not found.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """
        Processes the data by filtering entries and calculating averages.
        Returns a summary dictionary.
        """
        filtered_data = [entry for entry in data if entry.get('value') is not None]
        average_value = sum(entry['value'] for entry in filtered_data) / len(filtered_data) if filtered_data else 0
        summary = {
            'total_entries': len(data),
            'filtered_entries': len(filtered_data),
            'average_value': average_value
        }
        return summary

    def save_summary(self, summary):
        """
        Saves the summary to the output JSON file.
        """
        with open(self.output_file, 'w') as file:
            json.dump(summary, file, indent=4)

    def run(self):
        """
        Runs the data processing workflow: load, process, and save data.
        """
        data = self.load_data()
        summary = self.process_data(data)
        self.save_summary(summary)
        print(f"Summary saved to '{self.output_file}'.")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'output_summary.json')
    processor.run()