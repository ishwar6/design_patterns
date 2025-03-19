import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        """Initialize the DataProcessor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        """Read JSON data from the input file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Process the input data and return a summary of counts."""
        summary = {'total_items': len(data), 'categories': {}} 
        for item in data:
            category = item.get('category', 'Uncategorized')
            summary['categories'][category] = summary['categories'].get(category, 0) + 1
        return summary

    def save_summary(self, summary):
        """Save the summary data to the output file in JSON format."""
        with open(self.output_file, 'w') as file:
            json.dump(summary, file, indent=4)

    def run(self):
        """Execute the data processing workflow."""
        data = self.read_data()
        summary = self.process_data(data)
        self.save_summary(summary)
        print(f"Summary saved to {self.output_file}.")

if __name__ == '__main__':
    processor = DataProcessor('input_data.json', 'summary_output.json')
    processor.run()