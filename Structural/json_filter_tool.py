import json
import os

def load_json_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_data(data, key, value):
    return [item for item in data if item.get(key) == value]


def save_filtered_data(filtered_data, output_path):
    with open(output_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)


def process_json_file(input_path, output_path, filter_key, filter_value):
    data = load_json_data(input_path)
    filtered_data = filter_data(data, filter_key, filter_value)
    save_filtered_data(filtered_data, output_path)
    print(f"Filtered data saved to {output_path}")


if __name__ == '__main__':
    input_file = 'data.json'
    output_file = 'filtered_data.json'
    key_to_filter = 'category'
    value_to_filter = 'books'
    process_json_file(input_file, output_file, key_to_filter, value_to_filter)