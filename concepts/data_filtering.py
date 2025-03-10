# concepts/data_filter.py

from typing import List, Dict, Any

class DataFilter:
    """A class to filter data based on specified criteria."""
    
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        """
        Initializes the DataFilter with a list of dictionaries.

        Args:
            data (List[Dict[str, Any]]): A list of data entries to be filtered.
        """
        self.data = data

    def filter_by_field(self, field: str, value: Any) -> List[Dict[str, Any]]:
        """
        Filters the data entries based on a specified field and value.

        Args:
            field (str): The field name to filter by.
            value (Any): The value to match against.

        Returns:
            List[Dict[str, Any]]: A list of filtered data entries.
        """
        return [entry for entry in self.data if entry.get(field) == value]

    def filter_by_range(self, field: str, min_value: Any, max_value: Any) -> List[Dict[str, Any]]:
        """
        Filters the data entries based on a specified field and a range of values.

        Args:
            field (str): The field name to filter by.
            min_value (Any): The minimum value of the range.
            max_value (Any): The maximum value of the range.

        Returns:
            List[Dict[str, Any]]: A list of filtered data entries.
        """
        return [
            entry for entry in self.data
            if entry.get(field) is not None and min_value <= entry[field] <= max_value
        ]

    def filter_by_multiple_criteria(self, criteria: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Filters the data entries based on multiple criteria provided in a dictionary.

        Args:
            criteria (Dict[str, Any]): A dictionary where keys are field names and values are the values to match against.

        Returns:
            List[Dict[str, Any]]: A list of filtered data entries.
        """
        def matches_criteria(entry: Dict[str, Any]) -> bool:
            return all(entry.get(field) == value for field, value in criteria.items())

        return [entry for entry in self.data if matches_criteria(entry)]

# Sample Usage
if __name__ == "__main__":
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "New York"},
        {"name": "David", "age": 30, "city": "Chicago"},
    ]

    data_filter = DataFilter(sample_data)

    # Filter by field
    age_filtered = data_filter.filter_by_field("age", 30)
    print("Filtered by age 30:", age_filtered)

    # Filter by range
    age_range_filtered = data_filter.filter_by_range("age", 25, 30)
    print("Filtered by age between 25 and 30:", age_range_filtered)

    # Filter by multiple criteria
    criteria_filtered = data_filter.filter_by_multiple_criteria({"city": "New York", "age": 30})
    print("Filtered by city New York and age 30:", criteria_filtered)