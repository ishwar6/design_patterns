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

def main():
    data = {'name': 'John Doe', 'age': 30, 'city': 'New York'}
    filename = 'data.json'
    save_data_to_file(data, filename)
    loaded_data = load_data_from_file(filename)
    print('Loaded Data:', loaded_data)

if __name__ == '__main__':
    main()