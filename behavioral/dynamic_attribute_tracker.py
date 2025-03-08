# behavioral/attribute_tracker.py

class AttributeTracker:
    """
    A class used to track and manage attributes of objects dynamically.
    
    Attributes can be added, updated, retrieved, or removed. This allows 
    for a flexible way to handle attributes without the need for a fixed schema.
    
    Methods
    -------
    add_attribute(attr_name: str, value: any) -> None
        Adds a new attribute with the specified name and value.
        
    update_attribute(attr_name: str, value: any) -> None
        Updates the value of an existing attribute.
        
    get_attribute(attr_name: str) -> any
        Retrieves the value of the specified attribute.
        
    remove_attribute(attr_name: str) -> None
        Removes the attribute with the specified name.
        
    list_attributes() -> dict
        Returns a dictionary of all attributes and their values.
    """

    def __init__(self):
        self.attributes = {}

    def add_attribute(self, attr_name: str, value: any) -> None:
        """Adds a new attribute with the specified name and value."""
        if attr_name in self.attributes:
            raise ValueError(f"Attribute '{attr_name}' already exists.")
        self.attributes[attr_name] = value

    def update_attribute(self, attr_name: str, value: any) -> None:
        """Updates the value of an existing attribute."""
        if attr_name not in self.attributes:
            raise KeyError(f"Attribute '{attr_name}' does not exist.")
        self.attributes[attr_name] = value

    def get_attribute(self, attr_name: str) -> any:
        """Retrieves the value of the specified attribute."""
        if attr_name not in self.attributes:
            raise KeyError(f"Attribute '{attr_name}' does not exist.")
        return self.attributes[attr_name]

    def remove_attribute(self, attr_name: str) -> None:
        """Removes the attribute with the specified name."""
        if attr_name not in self.attributes:
            raise KeyError(f"Attribute '{attr_name}' does not exist.")
        del self.attributes[attr_name]

    def list_attributes(self) -> dict:
        """Returns a dictionary of all attributes and their values."""
        return self.attributes.copy()

# Sample Usage
if __name__ == "__main__":
    tracker = AttributeTracker()
    
    tracker.add_attribute('color', 'blue')
    tracker.add_attribute('size', 'large')
    
    print(tracker.list_attributes())  # Output: {'color': 'blue', 'size': 'large'}
    
    tracker.update_attribute('color', 'red')
    print(tracker.get_attribute('color'))  # Output: 'red'
    
    tracker.remove_attribute('size')
    print(tracker.list_attributes())  # Output: {'color': 'red'}