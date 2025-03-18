import json
import os

class ConfigManager:
    """
    A class to manage configuration settings using JSON files.
    """
    def __init__(self, config_file):
        """
        Initializes ConfigManager with a specific configuration file.
        """
        self.config_file = config_file
        self.load_config()

    def load_config(self):
        """
        Loads configuration from the JSON file.
        """
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as file:
                self.config = json.load(file)
        else:
            self.config = {}

    def get_value(self, key):
        """
        Retrieves a value from the configuration by key.
        """
        return self.config.get(key, None)

    def set_value(self, key, value):
        """
        Sets a value in the configuration and saves it to the file.
        """
        self.config[key] = value
        self.save_config()

    def save_config(self):
        """
        Saves the current configuration back to the JSON file.
        """
        with open(self.config_file, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    config_manager = ConfigManager('config.json')
    config_manager.set_value('api_key', '12345')
    print(config_manager.get_value('api_key'))
    config_manager.set_value('timeout', 30)
    print(config_manager.get_value('timeout'))
    print(config_manager.get_value('non_existing_key'))