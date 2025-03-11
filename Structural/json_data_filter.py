import json
import os

def read_json(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'File {file_path} not found.')
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_data(data, threshold):
    return [item for item in data if item.get('value', 0) > threshold]


def save_filtered_data(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)


def process_json(input_path, output_path, threshold):
    data = read_json(input_path)
    filtered_data = filter_data(data, threshold)
    save_filtered_data(filtered_data, output_path)
    print(f'Filtered data saved to {output_path}')


if __name__ == '__main__':
    input_file = 'data.json'
    output_file = 'filtered_data.json'
    threshold_value = 10
    process_json(input_file, output_file, threshold_value)