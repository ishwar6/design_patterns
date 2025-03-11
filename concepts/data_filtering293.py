import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_data(data, threshold):
    return [item for item in data if item['value'] > threshold]


def save_data(data, output_path):
    with open(output_path, 'w') as file:
        json.dump(data, file, indent=4)


def main(input_file, output_file, threshold):
    data = load_data(input_file)
    filtered_data = filter_data(data, threshold)
    save_data(filtered_data, output_file)
    print(f"Filtered data saved to {output_file}")


if __name__ == '__main__':
    input_path = 'data.json'
    output_path = 'filtered_data.json'
    threshold_value = 10
    main(input_path, output_path, threshold_value)