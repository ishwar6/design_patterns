import json

class DataProcessor:
    """
    A class to process and filter JSON data.
    """
    def __init__(self, data):
        """
        Initializes the DataProcessor with JSON data.
        """
        self.data = data

    def filter_data(self, threshold):
        """
        Filters the data based on a threshold value.
        Returns entries greater than the threshold.
        """
        return [entry for entry in self.data if entry['value'] > threshold]

    def save_filtered_data(self, filtered_data, output_file):
        """
        Saves the filtered data to a specified JSON file.
        """
        with open(output_file, 'w') as f:
            json.dump(filtered_data, f, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 5},
        {'id': 4, 'value': 30}
    ]
    processor = DataProcessor(sample_data)
    threshold_value = 15
    filtered = processor.filter_data(threshold_value)
    processor.save_filtered_data(filtered, 'filtered_data.json')
    print(f'Filtered data saved: {filtered}')