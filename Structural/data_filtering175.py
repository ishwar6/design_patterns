import json

class DataProcessor:
    """
    Processes and filters a dataset based on specified criteria.
    """
    def __init__(self, data):
        """
        Initializes the DataProcessor with the given data.
        :param data: List of dictionaries containing dataset.
        """
        self.data = data

    def filter_data(self, min_age, max_age):
        """
        Filters data entries based on age criteria.
        :param min_age: Minimum age for filtering.
        :param max_age: Maximum age for filtering.
        :return: List of filtered data entries.
        """
        return [entry for entry in self.data if min_age <= entry['age'] <= max_age]

    def save_to_file(self, filtered_data, filename):
        """
        Saves the filtered data to a JSON file.
        :param filtered_data: List of filtered data entries.
        :param filename: Name of the file to save the data.
        """
        with open(filename, 'w') as file:
            json.dump(filtered_data, file, indent=4)

if __name__ == '__main__':
    sample_data = [
        {'name': 'Alice', 'age': 30},
        {'name': 'Bob', 'age': 22},
        {'name': 'Charlie', 'age': 25},
        {'name': 'David', 'age': 35}
    ]
    processor = DataProcessor(sample_data)
    filtered = processor.filter_data(25, 30)
    processor.save_to_file(filtered, 'filtered_data.json')
    print(f'Filtered data saved: {filtered}')