import json
import os

class DataProcessor:
    def __init__(self, directory):
        """Initialize DataProcessor with a directory."""
        self.directory = directory

    def load_data(self, filename):
        """Load JSON data from a file."""
        with open(os.path.join(self.directory, filename), 'r') as file:
            return json.load(file)

    def process_data(self, data):
        """Process the loaded data to calculate statistics."""
        total = sum(data)
        count = len(data)
        mean = total / count if count > 0 else 0
        return {'total': total, 'count': count, 'mean': mean}

    def save_results(self, results, output_filename):
        """Save the processed results to a JSON file."""
        with open(os.path.join(self.directory, output_filename), 'w') as file:
            json.dump(results, file, indent=4)

    def run(self, input_filename, output_filename):
        """Load, process, and save data in one run."""
        data = self.load_data(input_filename)
        results = self.process_data(data)
        self.save_results(results, output_filename)
        print(f'Results saved to {output_filename}')

if __name__ == '__main__':
    processor = DataProcessor('./data')
    processor.run('input.json', 'output.json')