import json
from collections import defaultdict

class DataAggregator:
    def __init__(self):
        """
        Initializes the DataAggregator with an empty data structure.
        """
        self.data = defaultdict(list)

    def add_entry(self, category, value):
        """
        Adds a value to the specified category.
        :param category: The category to which the value belongs.
        :param value: The value to be added.
        """
        self.data[category].append(value)

    def get_summary(self):
        """
        Generates a summary of the aggregated data.
        :return: A dictionary with categories and their corresponding values.
        """
        return {category: sum(values) for category, values in self.data.items()}

    def save_to_file(self, filename):
        """
        Saves the aggregated data to a JSON file.
        :param filename: The name of the file to save the data.
        """
        with open(filename, 'w') as file:
            json.dump(self.get_summary(), file, indent=4)

if __name__ == '__main__':
    aggregator = DataAggregator()
    aggregator.add_entry('fruits', 10)
    aggregator.add_entry('fruits', 15)
    aggregator.add_entry('vegetables', 5)
    aggregator.add_entry('vegetables', 10)
    print(aggregator.get_summary())
    aggregator.save_to_file('aggregated_data.json')