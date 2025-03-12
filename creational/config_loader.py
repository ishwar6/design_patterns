import json
import os

class ConfigLoader:
    """Loads configuration from a JSON file."""
    def __init__(self, file_path):
        """Initializes ConfigLoader with the path to the config file."""
        self.file_path = file_path
        self.config_data = self.load_config()

    def load_config(self):
        """Reads the JSON file and returns the configuration data."""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"Configuration file not found: {self.file_path}")
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_value(self, key):
        """Retrieves a value from the configuration data by key."""
        return self.config_data.get(key, None)

    def save_config(self, new_data):
        """Saves updated configuration data back to the JSON file."""
        self.config_data.update(new_data)
        with open(self.file_path, 'w') as file:
            json.dump(self.config_data, file, indent=4)

if __name__ == '__main__':
    config_loader = ConfigLoader('config.json')
    print(config_loader.get_value('database_url'))
    config_loader.save_config({'database_url': 'mysql://localhost:3306/new_db'})