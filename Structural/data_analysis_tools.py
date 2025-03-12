import json

class DataProcessor:
    def __init__(self, data):
        """Initializes the DataProcessor with a data list."""
        self.data = data

    def filter_data(self, threshold):
        """Filters the data to include only values above the given threshold."""
        return [x for x in self.data if x > threshold]

    def calculate_average(self):
        """Calculates the average of the data list."""
        return sum(self.data) / len(self.data) if self.data else 0

    def to_json(self, filtered_data):
        """Converts the filtered data to a JSON string."""
        return json.dumps(filtered_data, indent=4)

if __name__ == '__main__':
    raw_data = [10, 20, 5, 30, 25, 15]
    processor = DataProcessor(raw_data)
    filtered = processor.filter_data(15)
    avg = processor.calculate_average()
    json_output = processor.to_json(filtered)
    print(f'Filtered Data: {filtered}')
    print(f'Average: {avg}')
    print(f'JSON Output: {json_output}')