import json
import os

def read_json_file(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def merge_json_files(input_files, output_file):
    merged_data = {}
    for file in input_files:
        data = read_json_file(file)
        merged_data.update(data)
    write_json_file(output_file, merged_data)


if __name__ == '__main__':
    input_files = ['data1.json', 'data2.json']
    output_file = 'merged_data.json'
    merge_json_files(input_files, output_file)
    print(f'Merged data written to {output_file}')