import json

class DataProcessor:
    """
    A class to process and analyze JSON data.
    """

    def __init__(self, json_file):
        """
        Initializes the DataProcessor with a JSON file.
        """
        self.json_file = json_file
        self.data = self.load_data()

    def load_data(self):
        """
        Loads JSON data from the specified file.
        """
        with open(self.json_file, 'r') as file:
            return json.load(file)

    def filter_data(self, key, value):
        """
        Filters the loaded data based on a key-value pair.
        """
        return [item for item in self.data if item.get(key) == value]

    def save_filtered_data(self, filtered_data, output_file):
        """
        Saves the filtered data to a specified output file.
        """
        with open(output_file, 'w') as file:
            json.dump(filtered_data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    filtered = processor.filter_data('status', 'active')
    processor.save_filtered_data(filtered, 'filtered_data.json')
    print(f'Filtered data saved to filtered_data.json with {len(filtered)} records.')