import json

class DataProcessor:
    """Processes input data and performs various transformations."""

    def __init__(self, data):
        """Initializes DataProcessor with input data."""
        self.data = data

    def filter_data(self, threshold):
        """Filters the data based on a threshold value."""
        return [item for item in self.data if item['value'] > threshold]

    def transform_data(self):
        """Transforms data by calculating square of values."""
        return [{**item, 'value': item['value'] ** 2} for item in self.data]

    def save_to_file(self, filename, data):
        """Saves the processed data to a JSON file."""
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

if __name__ == '__main__':
    input_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 5},
        {'id': 4, 'value': 25}
    ]
    processor = DataProcessor(input_data)
    filtered_data = processor.filter_data(threshold=10)
    transformed_data = processor.transform_data()
    processor.save_to_file('output.json', transformed_data)
    print('Filtered Data:', filtered_data)
    print('Transformed Data:', transformed_data)