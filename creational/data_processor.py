import json
import os

def save_data_to_file(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file)

def load_data_from_file(filename):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r') as file:
        return json.load(file)

def process_data(data):
    return {k: v * 2 for k, v in data.items()}

if __name__ == '__main__':
    input_data = {'a': 1, 'b': 2, 'c': 3}
    processed_data = process_data(input_data)
    output_file = 'output_data.json'
    save_data_to_file(processed_data, output_file)
    loaded_data = load_data_from_file(output_file)
    print('Processed Data:', loaded_data)