import json
import os

class DataProcessor:
    """
    A class to process and filter JSON data from files.
    """

    def __init__(self, input_dir, output_file):
        """
        Initializes the DataProcessor with an input directory and output file.
        """
        self.input_dir = input_dir
        self.output_file = output_file

    def load_data(self):
        """
        Loads and returns JSON data from all files in the input directory.
        """
        data = []
        for filename in os.listdir(self.input_dir):
            if filename.endswith('.json'):
                with open(os.path.join(self.input_dir, filename), 'r') as f:
                    data.append(json.load(f))
        return data

    def filter_data(self, data, key, value):
        """
        Filters the loaded data based on a key-value pair.
        """
        return [item for item in data if item.get(key) == value]

    def save_data(self, data):
        """
        Saves the filtered data to the specified output file in JSON format.
        """
        with open(self.output_file, 'w') as f:
            json.dump(data, f, indent=4)

    def process(self, filter_key, filter_value):
        """
        Executes the data processing workflow: load, filter, and save.
        """
        loaded_data = self.load_data()
        filtered_data = self.filter_data(loaded_data, filter_key, filter_value)
        self.save_data(filtered_data)
        print(f"Processed {len(loaded_data)} records, saved {len(filtered_data)} records to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('data', 'output.json')
    processor.process('status', 'active')