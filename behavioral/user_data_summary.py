import json
import os

class UserDataProcessor:
    """Processes user data from a JSON file and generates a summary report."""

    def __init__(self, input_file, output_file):
        """Initializes the processor with input and output file paths."""
        self.input_file = input_file
        self.output_file = output_file
        self.user_data = []

    def load_data(self):
        """Loads user data from a JSON file."""
        if not os.path.exists(self.input_file):
            raise FileNotFoundError(f"Input file {self.input_file} does not exist.")
        with open(self.input_file, 'r') as file:
            self.user_data = json.load(file)

    def generate_summary(self):
        """Generates a summary of user data highlighting count and average age."""
        if not self.user_data:
            raise ValueError("No user data loaded. Call load_data() first.")
        total_users = len(self.user_data)
        total_age = sum(user['age'] for user in self.user_data if 'age' in user)
        average_age = total_age / total_users if total_users > 0 else 0
        summary = {
            'total_users': total_users,
            'average_age': average_age
        }
        return summary

    def save_summary(self, summary):
        """Saves the summary report to a JSON file."""
        with open(self.output_file, 'w') as file:
            json.dump(summary, file, indent=4)

    def process(self):
        """Executes the data processing workflow."""
        self.load_data()
        summary = self.generate_summary()
        self.save_summary(summary)
        print(f"Summary saved to {self.output_file}")

if __name__ == '__main__':
    processor = UserDataProcessor('users.json', 'summary.json')
    processor.process()