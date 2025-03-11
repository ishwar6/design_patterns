import json
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        print(f'File not found: {file_path}')
        return None
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_data(data, threshold):
    return [item for item in data if item.get('value', 0) > threshold]


def main():
    input_file = 'input.json'
    output_file = 'output.json'
    threshold_value = 10

    data = read_json_file(input_file)
    if data is not None:
        filtered_data = filter_data(data, threshold_value)
        write_json_file(output_file, filtered_data)
        print(f'Filtered data written to: {output_file}')

if __name__ == '__main__':
    main()