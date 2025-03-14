import json

class DataProcessor:
    def __init__(self, file_path):
        """Initialize DataProcessor with a file path."""
        self.file_path = file_path

    def read_data(self):
        """Read JSON data from the file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def filter_data(self, key, value):
        """Filter data based on a key-value pair."""
        data = self.read_data()
        return [item for item in data if item.get(key) == value]

    def save_data(self, filtered_data, output_file):
        """Save filtered data to a new JSON file."""
        with open(output_file, 'w') as file:
            json.dump(filtered_data, file, indent=4)

if __name__ == '__main__':
    processor = DataProcessor('input_data.json')
    filtered = processor.filter_data('status', 'active')
    processor.save_data(filtered, 'filtered_data.json')
    print(f"Filtered data saved to 'filtered_data.json' with {len(filtered)} records.")