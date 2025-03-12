import json

class DataProcessor:
    """
    A class to process and analyze JSON data.
    """

    def __init__(self, data):
        """
        Initializes the DataProcessor with data.
        """
        self.data = data

    def filter_data(self, key, value):
        """
        Filters the data based on a specified key and value.
        """
        return [item for item in self.data if item.get(key) == value]

    def calculate_average(self, key):
        """
        Calculates the average of numerical values for a specified key.
        """
        total = sum(item.get(key, 0) for item in self.data)
        count = sum(1 for item in self.data if key in item)
        return total / count if count > 0 else 0

    def save_to_file(self, file_name):
        """
        Saves the processed data to a JSON file.
        """
        with open(file_name, 'w') as f:
            json.dump(self.data, f, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30, 'score': 88},
        {'name': 'Bob', 'age': 25, 'score': 95},
        {'name': 'Charlie', 'age': 30, 'score': 82},
        {'name': 'David', 'age': 25, 'score': 78}
    ]
    processor = DataProcessor(sample_data)
    filtered = processor.filter_data('age', 30)
    average_score = processor.calculate_average('score')
    processor.save_to_file('processed_data.json')
    print('Filtered Data:', filtered)
    print('Average Score:', average_score)