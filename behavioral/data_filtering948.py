import json
import os

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"{file_path} does not exist")
    with open(file_path, 'r') as file:
        return json.load(file)


def filter_data(data, key, value):
    return [entry for entry in data if entry.get(key) == value]


def save_filtered_data(filtered_data, output_path):
    with open(output_path, 'w') as file:
        json.dump(filtered_data, file, indent=4)


def main(input_path, output_path, filter_key, filter_value):
    data = load_data(input_path)
    filtered_data = filter_data(data, filter_key, filter_value)
    save_filtered_data(filtered_data, output_path)
    print(f"Filtered data saved to {output_path}")


if __name__ == '__main__':
    main('data.json', 'filtered_data.json', 'status', 'active')