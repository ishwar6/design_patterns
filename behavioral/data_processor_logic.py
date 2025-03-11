import json
import os

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def load_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        processed = {k: v for k, v in data.items() if isinstance(v, (int, float))}
        return {k: v * 2 for k, v in processed.items()}

    def save_data(self, data):
        with open(self.output_file, 'w') as file:
            json.dump(data, file, indent=4)

    def run(self):
        data = self.load_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)

if __name__ == '__main__':
    input_path = 'input_data.json'
    output_path = 'output_data.json'
    if os.path.exists(input_path):
        processor = DataProcessor(input_path, output_path)
        processor.run()
        print(f'Processed data saved to {output_path}')
    else:
        print('Input file does not exist.')