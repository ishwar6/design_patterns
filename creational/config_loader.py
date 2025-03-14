import json
from typing import Dict, Any

class ConfigurationLoader:
    """Loads configuration from a JSON file."""
    def __init__(self, file_path: str) -> None:
        """Initializes the loader with a file path."""
        self.file_path = file_path
        self.config = self.load_config()

    def load_config(self) -> Dict[str, Any]:
        """Loads and returns the configuration data from the JSON file."""
        with open(self.file_path, 'r') as file:
            return json.load(file)

    def get_value(self, key: str) -> Any:
        """Retrieves a value from the configuration by key."""
        return self.config.get(key, None)

    def update_value(self, key: str, value: Any) -> None:
        """Updates a value in the configuration and saves the changes to the file."""
        self.config[key] = value
        with open(self.file_path, 'w') as file:
            json.dump(self.config, file, indent=4)

if __name__ == '__main__':
    config_loader = ConfigurationLoader('config.json')
    print(config_loader.get_value('database'))
    config_loader.update_value('database', 'new_database')
    print(config_loader.get_value('database'))