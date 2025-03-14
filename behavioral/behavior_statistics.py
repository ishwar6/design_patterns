import csv
from collections import defaultdict

class BehaviorAnalyzer:
    """
    Analyzes behavioral data from a CSV file and generates summary statistics.
    """

    def __init__(self, file_path):
        """Initializes the analyzer with the path to the CSV file."""
        self.file_path = file_path
        self.data = defaultdict(list)

    def load_data(self):
        """Loads data from the CSV file into a dictionary."""
        with open(self.file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                self.data[row['user_id']].append(float(row['behavior_value']))

    def calculate_statistics(self):
        """Calculates mean and standard deviation for each user."""
        statistics = {}
        for user_id, values in self.data.items():
            mean_value = sum(values) / len(values)
            variance = sum((x - mean_value) ** 2 for x in values) / len(values)
            std_deviation = variance ** 0.5
            statistics[user_id] = {'mean': mean_value, 'std_dev': std_deviation}
        return statistics

    def generate_report(self, output_path):
        """Generates a report of statistics and saves it to a file."""
        statistics = self.calculate_statistics()
        with open(output_path, mode='w') as file:
            writer = csv.writer(file)
            writer.writerow(['user_id', 'mean', 'std_dev'])
            for user_id, stats in statistics.items():
                writer.writerow([user_id, stats['mean'], stats['std_dev']])
        print(f'Report generated at {output_path}')

if __name__ == '__main__':
    analyzer = BehaviorAnalyzer('behavior_data.csv')
    analyzer.load_data()
    analyzer.generate_report('behavior_report.csv')