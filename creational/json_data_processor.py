import json

class DataProcessor:
    """
    A class to process and analyze JSON data.
    """

    def __init__(self, data):
        """
        Initializes the DataProcessor with JSON data.
        """
        self.data = json.loads(data)

    def filter_data(self, key, threshold):
        """
        Filters data entries based on a specified key and threshold.
        """
        return [entry for entry in self.data if entry.get(key, 0) > threshold]

    def summarize_data(self, key):
        """
        Summarizes the total for a specified key in the data.
        """
        return sum(entry.get(key, 0) for entry in self.data)

if __name__ == '__main__':
    json_data = '''[
        {"name": "Alice", "age": 30, "score": 85},
        {"name": "Bob", "age": 22, "score": 90},
        {"name": "Charlie", "age": 25, "score": 70}
    ]'''  
    processor = DataProcessor(json_data)
    filtered = processor.filter_data('score', 80)
    total_score = processor.summarize_data('score')
    print('Filtered Data:', filtered)
    print('Total Score:', total_score)