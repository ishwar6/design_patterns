python
class Feature:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display(self):
        return f'Feature: {self.name}\nDescription: {self.description}'

    def is_active(self):
        # Placeholder for a method that determines if the feature is active
        return True