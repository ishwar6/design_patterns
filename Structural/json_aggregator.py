import json
import os

class DataAggregator:
    """Aggregates data from multiple JSON files into a single report."""
    def __init__(self, directory):
        """Initializes the DataAggregator with a directory to search for JSON files."""
        self.directory = directory
        self.data = []

    def load_data(self):
        """Loads data from all JSON files in the specified directory."""
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    self.data.append(json.load(file))

    def aggregate(self):
        """Aggregates loaded data into a single dictionary summarizing the values."""
        aggregated_data = {}
        for entry in self.data:
            for key, value in entry.items():
                if key in aggregated_data:
                    aggregated_data[key] += value
                else:
                    aggregated_data[key] = value
        return aggregated_data

    def save_report(self, output_file):
        """Saves the aggregated report to a specified output file."""
        aggregated_data = self.aggregate()
        with open(output_file, 'w') as file:
            json.dump(aggregated_data, file, indent=4)

if __name__ == '__main__':
    aggregator = DataAggregator('data')
    aggregator.load_data()
    aggregator.save_report('output/report.json')