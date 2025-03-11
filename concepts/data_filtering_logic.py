import json

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def filter_data(self, threshold):
        return [item for item in self.data if item['value'] > threshold]

    def calculate_average(self, filtered_data):
        total = sum(item['value'] for item in filtered_data)
        return total / len(filtered_data) if filtered_data else 0

    def process(self, threshold):
        filtered = self.filter_data(threshold)
        average = self.calculate_average(filtered)
        return filtered, average

if __name__ == '__main__':
    sample_data = [
        {'id': 1, 'value': 10},
        {'id': 2, 'value': 20},
        {'id': 3, 'value': 30},
        {'id': 4, 'value': 5}
    ]
    processor = DataProcessor(sample_data)
    result, avg = processor.process(15)
    print('Filtered Data:', json.dumps(result, indent=2))
    print('Average Value:', avg)