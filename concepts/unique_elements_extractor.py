# concepts/unique_elements.py

from typing import List, Any

class UniqueElements:
    """A class to handle operations for retrieving unique elements from a list."""
    
    @staticmethod
    def get_unique_elements(input_list: List[Any]) -> List[Any]:
        """Return a list of unique elements from the provided input list.

        Args:
            input_list (List[Any]): A list from which to extract unique elements.

        Returns:
            List[Any]: A list containing only unique elements, preserving the order of first appearance.
        """
        seen = set()
        unique_list = []
        for element in input_list:
            if element not in seen:
                seen.add(element)
                unique_list.append(element)
        return unique_list

    @staticmethod
    def get_unique_elements_count(input_list: List[Any]) -> int:
        """Return the count of unique elements in the provided input list.

        Args:
            input_list (List[Any]): A list from which to count unique elements.

        Returns:
            int: The number of unique elements in the list.
        """
        unique_elements = UniqueElements.get_unique_elements(input_list)
        return len(unique_elements)

# Sample Usage
if __name__ == "__main__":
    input_data = [1, 2, 2, 3, 4, 4, 5]
    unique_elements = UniqueElements.get_unique_elements(input_data)
    unique_count = UniqueElements.get_unique_elements_count(input_data)

    print("Unique elements:", unique_elements)  # Output: Unique elements: [1, 2, 3, 4, 5]
    print("Count of unique elements:", unique_count)  # Output: Count of unique elements: 5