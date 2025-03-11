import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        return {key: value for key, value in data.items() if isinstance(value, (int, float))}

    def save_data(self, processed_data):
        with open(self.output_file, 'w') as file:
            json.dump(processed_data, file, indent=4)

    def run(self):
        raw_data = self.read_data()
        processed_data = self.process_data(raw_data)
        self.save_data(processed_data)

if __name__ == '__main__':
    input_file = 'input.json'
    output_file = 'output.json'
    processor = DataProcessor(input_file, output_file)
    processor.run()
    print(f'Processed data saved to {output_file}')