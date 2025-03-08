# concepts/unique_finder.py

from typing import List, Any, Set

class UniqueElementFinder:
    """
    A class to find unique elements in a list while maintaining the order.
    """
    
    def __init__(self, elements: List[Any]):
        """
        Initializes the UniqueElementFinder with a list of elements.

        :param elements: The initial list of elements. 
        """
        self.elements = elements

    def find_unique(self) -> List[Any]:
        """
        Returns a list of unique elements from the initialized elements while
        maintaining the order of their first occurrence.

        :return: A list of unique elements.
        """
        seen: Set[Any] = set()
        unique_elements: List[Any] = []
        
        for element in self.elements:
            if element not in seen:
                seen.add(element)
                unique_elements.append(element)
        
        return unique_elements

def main():
    """
    Example usage of the UniqueElementFinder class.
    """
    sample_list = [1, 2, 2, 3, 4, 4, 5, 1, 2]
    finder = UniqueElementFinder(sample_list)
    unique_items = finder.find_unique()
    
    print(f"Unique elements: {unique_items}")

if __name__ == "__main__":
    main()