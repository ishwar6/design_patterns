# behavior_analysis.py

from collections import defaultdict
from typing import List, Dict, Any, Tuple

class BehaviorAnalyzer:
    """A class to analyze and extract insights from behavioral data."""
    
    def __init__(self, data: List[Dict[str, Any]]) -> None:
        """
        Initializes the BehaviorAnalyzer with data.

        Args:
            data (List[Dict[str, Any]]): A list of dictionaries containing behavioral data.
        """
        self.data = data

    def filter_by_event(self, event_name: str) -> List[Dict[str, Any]]:
        """
        Filters the dataset by a specified event name.

        Args:
            event_name (str): The name of the event to filter by.

        Returns:
            List[Dict[str, Any]]: A filtered list of behavioral records.
        """
        return [record for record in self.data if record.get('event') == event_name]

    def count_event_occurrences(self) -> Dict[str, int]:
        """
        Counts occurrences of each event in the dataset.

        Returns:
            Dict[str, int]: A dictionary with events as keys and their counts as values.
        """
        event_counts = defaultdict(int)
        for record in self.data:
            event = record.get('event')
            if event:
                event_counts[event] += 1
        return dict(event_counts)

    def get_average_duration(self, event_name: str) -> float:
        """
        Calculates the average duration of a specified event.

        Args:
            event_name (str): The event name to calculate the average duration for.

        Returns:
            float: The average duration of the event, or -1 if the event has no occurrences.
        """
        filtered_records = self.filter_by_event(event_name)
        total_duration = sum(record.get('duration', 0) for record in filtered_records)
        count = len(filtered_records)
        return total_duration / count if count > 0 else -1

def sample_usage() -> None:
    """Function demonstrating sample usage of BehaviorAnalyzer."""
    sample_data = [
        {'event': 'click', 'duration': 2.4},
        {'event': 'scroll', 'duration': 1.2},
        {'event': 'click', 'duration': 2.8},
        {'event': 'hover', 'duration': 0.5},
        {'event': 'scroll', 'duration': 1.5}
    ]
    
    analyzer = BehaviorAnalyzer(sample_data)
    
    print("Filtered Click Events:", analyzer.filter_by_event('click'))
    print("Event Occurrences:", analyzer.count_event_occurrences())
    print("Average Duration for Click Events:", analyzer.get_average_duration('click'))

if __name__ == "__main__":
    sample_usage()