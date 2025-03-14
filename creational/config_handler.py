import json
from pathlib import Path

class ConfigManager:
    """
    Manages application configuration loading and saving.
    """
    def __init__(self, config_file):
        """
        Initializes ConfigManager with a config file path.
        """
        self.config_file = Path(config_file)
        self.config = self.load_config()

    def load_config(self):
        """
        Loads configuration from the JSON file.
        """
        if not self.config_file.exists():
            return {}
        with open(self.config_file, 'r') as file:
            return json.load(file)

    def save_config(self, new_config):
        """
        Saves the new configuration to the JSON file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(new_config, file, indent=4)

    def update_config(self, key, value):
        """
        Updates a specific key in the configuration.
        """
        self.config[key] = value
        self.save_config(self.config)

if __name__ == '__main__':
    config_manager = ConfigManager('config.json')
    config_manager.update_config('theme', 'dark')
    print('Updated config:', config_manager.config)