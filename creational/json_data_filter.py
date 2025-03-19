import json

class DataProcessor:
    """Processes data from a JSON file."""
    def __init__(self, file_path):
        """Initializes the DataProcessor with a file path."""
        self.file_path = file_path

    def load_data(self):
        """Loads data from the JSON file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, data, key, value):
        """Filters the loaded data based on a key-value pair."""
        return [item for item in data if item.get(key) == value]

    def save_data(self, data, output_path):
        """Saves the filtered data to a new JSON file."""
        with open(output_path, 'w') as file:
            json.dump(data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('data.json')
    data = processor.load_data()
    filtered_data = processor.filter_data(data, 'status', 'active')
    processor.save_data(filtered_data, 'filtered_data.json')
    print(f'Filtered data saved to filtered_data.json with {len(filtered_data)} entries.')