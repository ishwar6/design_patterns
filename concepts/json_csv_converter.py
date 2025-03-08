# concepts/data_converter.py

import json
import csv
from typing import List, Dict, Any

class DataConverter:
    """A class to convert data between JSON and CSV formats."""

    @staticmethod
    def json_to_csv(json_data: List[Dict[str, Any]], output_file: str) -> None:
        """Convert a list of dictionaries (JSON) to a CSV file.
        
        Args:
            json_data (List[Dict[str, Any]]): The JSON data to convert.
            output_file (str): The path to the output CSV file.
        
        Raises:
            ValueError: If json_data is empty or not a list.
        """
        if not isinstance(json_data, list) or not json_data:
            raise ValueError("Input must be a non-empty list of dictionaries.")
        
        with open(output_file, mode='w', newline='', encoding='utf-8') as csvfile:
            fieldnames = json_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for row in json_data:
                writer.writerow(row)

    @staticmethod
    def csv_to_json(csv_file: str) -> List[Dict[str, Any]]:
        """Convert a CSV file to a list of dictionaries (JSON).
        
        Args:
            csv_file (str): The path to the input CSV file.
        
        Returns:
            List[Dict[str, Any]]: The parsed data as a list of dictionaries.
        
        Raises:
            FileNotFoundError: If the CSV file does not exist.
        """
        try:
            with open(csv_file, mode='r', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                return [row for row in reader]
        except FileNotFoundError:
            raise FileNotFoundError(f"The file {csv_file} was not found.")


# Sample usage
if __name__ == "__main__":
    sample_json_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    # Convert JSON to CSV
    DataConverter.json_to_csv(sample_json_data, 'sample_output.csv')
    
    # Convert CSV back to JSON
    json_output = DataConverter.csv_to_json('sample_output.csv')
    print(json.dumps(json_output, indent=4))