import csv
from typing import List, Dict

class CSVProcessor:
    """
    Processes CSV files to filter and transform data.
    """
    def __init__(self, input_file: str, output_file: str) -> None:
        """
        Initializes the CSVProcessor with input and output file paths.
        """
        self.input_file = input_file
        self.output_file = output_file

    def read_csv(self) -> List[Dict[str, str]]:
        """
        Reads the CSV file and returns a list of dictionaries representing rows.
        """
        with open(self.input_file, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return [row for row in reader]

    def filter_data(self, data: List[Dict[str, str]], key: str, value: str) -> List[Dict[str, str]]:
        """
        Filters the data based on a given key-value pair.
        """
        return [row for row in data if row.get(key) == value]

    def write_csv(self, data: List[Dict[str, str]]) -> None:
        """
        Writes the filtered data to the output CSV file.
        """
        with open(self.output_file, mode='w', newline='', encoding='utf-8') as file:
            if data:
                writer = csv.DictWriter(file, fieldnames=data[0].keys())
                writer.writeheader()
                writer.writerows(data)

    def process(self, filter_key: str, filter_value: str) -> None:
        """
        Orchestrates the reading, filtering, and writing of CSV data.
        """
        data = self.read_csv()
        filtered_data = self.filter_data(data, filter_key, filter_value)
        self.write_csv(filtered_data)

if __name__ == '__main__':
    processor = CSVProcessor('input.csv', 'output.csv')
    processor.process('status', 'active')