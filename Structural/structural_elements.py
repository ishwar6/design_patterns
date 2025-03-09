# structural/example_feature.py

"""
This module provides a feature to manage a collection of structural elements,
such as beams and columns, by allowing users to add, remove, and list these
elements. Each structural element is represented by a class that includes
attributes like name, type, and dimensions. The management system ensures
that elements are valid and handles duplicate entries gracefully.
"""

class StructuralElement:
    """
    Represents a structural element with a name, type, and dimensions.
    
    Attributes:
        name (str): The name of the structural element.
        element_type (str): The type of structural element (e.g., 'beam', 'column').
        dimensions (dict): A dictionary containing dimensions (e.g., length, width, height).
    """
    
    def __init__(self, name: str, element_type: str, dimensions: dict):
        self.name = name
        self.element_type = element_type
        self.dimensions = dimensions

    def __repr__(self):
        return f"{self.element_type.capitalize()}(name='{self.name}', dimensions={self.dimensions})"


class StructuralManager:
    """
    Manages a collection of StructuralElement instances.
    
    Attributes:
        elements (list): List of structural elements being managed.
    """
    
    def __init__(self):
        self.elements = []

    def add_element(self, element: StructuralElement) -> None:
        """
        Adds a structural element to the collection.
        
        Parameters:
            element (StructuralElement): The structural element to add.
        
        Raises:
            ValueError: If the structural element already exists.
        """
        if any(e.name == element.name for e in self.elements):
            raise ValueError(f"Element with name '{element.name}' already exists.")
        self.elements.append(element)

    def remove_element(self, name: str) -> bool:
        """
        Removes a structural element from the collection by name.
        
        Parameters:
            name (str): The name of the structural element to remove.
        
        Returns:
            bool: True if the element was removed, False if it was not found.
        """
        for index, element in enumerate(self.elements):
            if element.name == name:
                del self.elements[index]
                return True
        return False

    def list_elements(self) -> list:
        """
        Lists all structural elements in the collection.
        
        Returns:
            list: A list of structural elements.
        """
        return self.elements


# Sample usage
if __name__ == "__main__":
    manager = StructuralManager()
    
    beam = StructuralElement("Beam1", "beam", {"length": 5.0, "width": 0.3, "height": 0.2})
    column = StructuralElement("Column1", "column", {"height": 3.0, "diameter": 0.5})
    
    manager.add_element(beam)
    manager.add_element(column)
    
    print("Elements after adding:")
    print(manager.list_elements())
    
    manager.remove_element("Beam1")
    
    print("Elements after removing Beam1:")
    print(manager.list_elements())