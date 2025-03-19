import json
import os

class DataProcessor:
    """Processes and analyzes data from a given JSON file."""

    def __init__(self, file_path):
        """Initializes DataProcessor with a file path."""
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Loads data from a JSON file and returns it as a dictionary."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_average(self, key):
        """Calculates the average of values associated with the given key in the data."""
        total = sum(item[key] for item in self.data if key in item)
        count = sum(1 for item in self.data if key in item)
        return total / count if count > 0 else 0

    def save_summary(self, output_path):
        """Saves a summary of the data analysis to a specified output path."""
        summary = {"average": self.get_average('value')}
        with open(output_path, 'w') as file:
            json.dump(summary, file)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    print(processor.get_average('value'))
    processor.save_summary('summary.json')