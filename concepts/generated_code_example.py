python
class Feature:
    def __init__(self, name):
        self.name = name
        self.enabled = False
    
    def enable(self):
        self.enabled = True
    
    def disable(self):
        self.enabled = False
    
    def is_enabled(self):
        return self.enabled

    def __str__(self):
        return f"Feature(name={self.name}, enabled={self.enabled})"