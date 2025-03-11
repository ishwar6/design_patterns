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
        results = []
        for item in data:
            if 'value' in item and item['value'] > 10:
                results.append({'id': item['id'], 'value': item['value'] * 2})
        return results

    def write_data(self, data):
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def execute(self):
        data = self.read_data()
        processed_data = self.process_data(data)
        self.write_data(processed_data)

if __name__ == '__main__':
    input_path = 'input.json'
    output_path = 'output.json'
    if os.path.exists(input_path):
        processor = DataProcessor(input_path, output_path)
        processor.execute()
        print(f'Processed data written to {output_path}')
    else:
        print('Input file does not exist.')