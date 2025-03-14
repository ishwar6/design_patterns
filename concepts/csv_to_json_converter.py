import csv
import json

class CsvToJsonConverter:
    """Converts CSV data to JSON format."""

    def __init__(self, csv_file, json_file):
        """Initializes the converter with CSV and JSON file paths."""
        self.csv_file = csv_file
        self.json_file = json_file

    def read_csv(self):
        """Reads the CSV file and returns a list of dictionaries."""
        with open(self.csv_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return list(reader)

    def write_json(self, data):
        """Writes the data to a JSON file."""
        with open(self.json_file, mode='w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)

    def convert(self):
        """Handles the conversion process from CSV to JSON."""
        data = self.read_csv()
        self.write_json(data)
        print(f'Converted {self.csv_file} to {self.json_file}')

if __name__ == '__main__':
    converter = CsvToJsonConverter('data.csv', 'data.json')
    converter.convert()