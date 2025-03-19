import json

class DataProcessor:
    """
    A class to process and transform JSON data.
    """

    def __init__(self, data):
        """
        Initialize DataProcessor with JSON data.
        """
        self.data = json.loads(data)

    def filter_data(self, key, value):
        """
        Filter the data based on a specific key-value pair.
        """
        return [item for item in self.data if item.get(key) == value]

    def sort_data(self, key):
        """
        Sort the data based on a specific key.
        """
        return sorted(self.data, key=lambda x: x.get(key))

    def save_to_file(self, filename):
        """
        Save the processed data to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self.data, file, indent=4)

if __name__ == '__main__':
    json_data = '[{"name": "Alice", "age": 30}, {"name": "Bob", "age": 25}, {"name": "Charlie", "age": 35}]'
    processor = DataProcessor(json_data)
    filtered = processor.filter_data('age', 30)
    sorted_data = processor.sort_data('name')
    processor.save_to_file('output.json')
    print("Filtered Data:", filtered)
    print("Sorted Data:", sorted_data)