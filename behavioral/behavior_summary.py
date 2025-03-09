# behavioral/behavior_tracker.py

from typing import List, Dict, Any, Optional

class BehaviorTracker:
    """
    A class to track and analyze user behaviors over time.
    
    Attributes:
        behaviors (Dict[str, List[Dict[str, Any]]]): A dictionary that maps user IDs to a list of behavior events.
    """
    
    def __init__(self):
        """Initialize an empty behavior tracker."""
        self.behaviors = {}
    
    def add_behavior(self, user_id: str, behavior: str, timestamp: Optional[str] = None) -> None:
        """
        Add a behavior event for a given user.
        
        Parameters:
            user_id (str): The ID of the user.
            behavior (str): A description of the behavior event.
            timestamp (Optional[str]): An optional timestamp of when the behavior occurred. 
                                       If not provided, the current time will be used.
        """
        if user_id not in self.behaviors:
            self.behaviors[user_id] = []
        
        event = {
            'behavior': behavior,
            'timestamp': timestamp
        }
        self.behaviors[user_id].append(event)

    def get_user_behaviors(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve the list of behavior events for a specific user.
        
        Parameters:
            user_id (str): The ID of the user.
        
        Returns:
            List[Dict[str, Any]]: A list of behavior events associated with the user.
        """
        return self.behaviors.get(user_id, [])

    def summarize_behaviors(self) -> Dict[str, int]:
        """
        Summarize the number of behaviors recorded for each user.
        
        Returns:
            Dict[str, int]: A dictionary mapping user IDs to the count of their behavior events.
        """
        return {user_id: len(events) for user_id, events in self.behaviors.items()}

# Sample usage

if __name__ == "__main__":
    tracker = BehaviorTracker()
    
    tracker.add_behavior("user_1", "login")
    tracker.add_behavior("user_1", "view_page", "2023-10-01T12:00:00")
    tracker.add_behavior("user_2", "logout", "2023-10-01T12:05:00")
    
    print("User 1 behaviors:")
    print(tracker.get_user_behaviors("user_1"))
    
    print("Behavior summary:")
    print(tracker.summarize_behaviors())