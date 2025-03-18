import csv
import json

class DataConverter:
    """Converts CSV data to JSON format."""
    def __init__(self, csv_file, json_file):
        """Initializes the DataConverter with input and output file paths."""
        self.csv_file = csv_file
        self.json_file = json_file

    def read_csv(self):
        """Reads data from a CSV file and returns it as a list of dictionaries."""
        with open(self.csv_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def write_json(self, data):
        """Writes data to a JSON file."""
        with open(self.json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def convert(self):
        """Converts the CSV data to JSON format and saves it to a file."""
        data = self.read_csv()
        self.write_json(data)
        print(f'Converted {self.csv_file} to {self.json_file}')

if __name__ == '__main__':
    converter = DataConverter('input.csv', 'output.json')
    converter.convert()