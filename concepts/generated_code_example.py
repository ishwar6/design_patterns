python
class Feature:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enabled = True

    def enable(self):
        self.enabled = True

    def disable(self):
        self.enabled = False

    def is_enabled(self):
        return self.enabled

    def get_details(self):
        return {
            "name": self.name,
            "description": self.description,
            "enabled": self.enabled
        }