# behavioral/behavior_tracker.py

class BehaviorTracker:
    """
    A class to track and analyze behaviors over time.
    
    Attributes:
        behaviors (dict): A dictionary to hold behaviors and their associated counts.
    """

    def __init__(self):
        """Initializes an empty behavior tracker."""
        self.behaviors = {}

    def add_behavior(self, behavior: str) -> None:
        """
        Adds a behavior to the tracker and increments its count.
        
        Parameters:
            behavior (str): The behavior to be added.
        """
        if not isinstance(behavior, str) or not behavior.strip():
            raise ValueError("Behavior must be a non-empty string.")
        self.behaviors[behavior] = self.behaviors.get(behavior, 0) + 1

    def get_behavior_count(self, behavior: str) -> int:
        """
        Retrieves the count of a specific behavior.
        
        Parameters:
            behavior (str): The behavior to retrieve the count for.
        
        Returns:
            int: The count of the specified behavior.
        """
        return self.behaviors.get(behavior, 0)

    def most_frequent_behavior(self) -> str:
        """
        Identifies the most frequently recorded behavior.
        
        Returns:
            str: The most frequent behavior or None if no behaviors are recorded.
        """
        if not self.behaviors:
            return None
        return max(self.behaviors, key=self.behaviors.get)

    def behavior_summary(self) -> dict:
        """
        Provides a summary of all tracked behaviors and their counts.
        
        Returns:
            dict: A dictionary of behaviors and their counts.
        """
        return dict(self.behaviors)


# Sample Usage
if __name__ == "__main__":
    tracker = BehaviorTracker()
    tracker.add_behavior("Exercise")
    tracker.add_behavior("Reading")
    tracker.add_behavior("Exercise")
    
    print(f"Exercise Count: {tracker.get_behavior_count('Exercise')}")
    print(f"Reading Count: {tracker.get_behavior_count('Reading')}")
    print(f"Most Frequent Behavior: {tracker.most_frequent_behavior()}")
    print(f"Behavior Summary: {tracker.behavior_summary()}")