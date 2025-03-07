python
class Feature:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        return f"Feature: {self.name}\nDescription: {self.description}"

    def is_valid(self):
        return bool(self.name) and bool(self.description)