# behavioral/behavior_tracker.py

class BehaviorTracker:
    """Tracks user behaviors and generates summaries over specified time intervals."""

    def __init__(self):
        """Initialize the BehaviorTracker with an empty list of behaviors."""
        self.behaviors = []

    def log_behavior(self, behavior: str) -> None:
        """Log a new behavior with the current timestamp.

        Args:
            behavior (str): A description of the behavior to log.
        """
        from datetime import datetime
        timestamp = datetime.now()
        self.behaviors.append((timestamp, behavior))

    def get_summary(self, start_time=None, end_time=None) -> list:
        """Get a summary of logged behaviors within a specified time interval.

        Args:
            start_time (datetime, optional): The start time for filtering behaviors.
            end_time (datetime, optional): The end time for filtering behaviors.

        Returns:
            list: A list of behaviors logged between start_time and end_time.
        """
        filtered_behaviors = []
        for timestamp, behavior in self.behaviors:
            if (start_time is None or timestamp >= start_time) and \
               (end_time is None or timestamp <= end_time):
                filtered_behaviors.append((timestamp, behavior))
        return filtered_behaviors

    def clear_logs(self) -> None:
        """Clear all logged behaviors."""
        self.behaviors.clear()


if __name__ == "__main__":
    from datetime import datetime, timedelta

    tracker = BehaviorTracker()
    
    tracker.log_behavior("User logged in")
    tracker.log_behavior("User viewed profile")
    tracker.log_behavior("User logged out")

    # Simulate a time interval
    start = datetime.now() - timedelta(days=1)
    end = datetime.now()

    summary = tracker.get_summary(start, end)
    for timestamp, behavior in summary:
        print(f"[{timestamp}] {behavior}")