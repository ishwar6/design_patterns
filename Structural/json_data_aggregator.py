import os
import json

class DataProcessor:
    """
    A class to process and analyze data from JSON files.
    """

    def __init__(self, directory):
        """
        Initializes the DataProcessor with a directory path.
        """
        self.directory = directory
        self.data = []

    def load_data(self):
        """
        Loads JSON data from all files in the specified directory.
        """
        for filename in os.listdir(self.directory):
            if filename.endswith('.json'):
                with open(os.path.join(self.directory, filename), 'r') as file:
                    self.data.append(json.load(file))

    def aggregate_data(self):
        """
        Aggregates data into a single dictionary summing values by key.
        """
        aggregated = {}
        for entry in self.data:
            for key, value in entry.items():
                if key in aggregated:
                    aggregated[key] += value
                else:
                    aggregated[key] = value
        return aggregated

    def save_aggregated_data(self, output_file):
        """
        Saves the aggregated data to a JSON file.
        """
        aggregated_data = self.aggregate_data()
        with open(output_file, 'w') as file:
            json.dump(aggregated_data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data')
    processor.load_data()
    processor.save_aggregated_data('output/aggregated_data.json')