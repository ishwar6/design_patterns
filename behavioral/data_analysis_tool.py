import json
import os

class DataProcessor:
    """Processes and analyzes data from a JSON file."""

    def __init__(self, file_path):
        """Initializes DataProcessor with a file path."""
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        """Loads data from a JSON file and returns it as a dictionary."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"{self.file_path} does not exist")
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_average(self, key):
        """Calculates the average value of a specified key in the data."""
        values = [item[key] for item in self.data if key in item]
        return sum(values) / len(values) if values else 0

    def save_summary(self, output_path):
        """Saves the average values of all numerical keys to a summary file."""
        summary = {key: self.get_average(key) for key in self.data[0].keys() if isinstance(self.data[0][key], (int, float))}
        with open(output_path, 'w') as file:
            json.dump(summary, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    processor.save_summary('summary.json')