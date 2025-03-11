import json
import os

def read_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_data(data, threshold):
    return [item for item in data if item['value'] > threshold]


def save_filtered_data(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)


def process_json_data(input_path, output_path, threshold):
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"{input_path} does not exist")
    data = read_json_file(input_path)
    filtered_data = filter_data(data, threshold)
    save_filtered_data(filtered_data, output_path)
    print(f"Filtered data saved to {output_path}")


if __name__ == '__main__':
    input_file = 'data.json'
    output_file = 'filtered_data.json'
    value_threshold = 10
    process_json_data(input_file, output_file, value_threshold)