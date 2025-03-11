import json

class DataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def read_data(self):
        with open(self.input_file, 'r') as file:
            return json.load(file)

    def process_data(self, data):
        return {key: value * 2 for key, value in data.items()}

    def save_data(self, processed_data):
        with open(self.output_file, 'w') as file:
            json.dump(processed_data, file, indent=2)

    def execute(self):
        data = self.read_data()
        processed_data = self.process_data(data)
        self.save_data(processed_data)

if __name__ == '__main__':
    processor = DataProcessor('input.json', 'output.json')
    processor.execute()