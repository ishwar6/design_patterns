python
class Feature:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def display_info(self):
        return f"Feature: {self.name}, Description: {self.description}"
    
    def is_enabled(self):
        return True

def feature_list():
    return [
        Feature("Feature A", "Description of Feature A"),
        Feature("Feature B", "Description of Feature B"),
        Feature("Feature C", "Description of Feature C"),
    ]