# behavioral/user_behavior_tracker.py

from collections import defaultdict
from typing import List, Dict, Any

class UserBehaviorTracker:
    """
    A class to track and analyze user behaviors within an application.
    
    Attributes:
        user_data (defaultdict): A dictionary to store user actions.
    """
    
    def __init__(self) -> None:
        """Initializes the UserBehaviorTracker with an empty user_data dictionary."""
        self.user_data = defaultdict(list)

    def add_user_action(self, user_id: str, action: str, timestamp: str) -> None:
        """
        Records an action performed by a user.

        Args:
            user_id (str): The unique identifier of the user.
            action (str): The action performed by the user.
            timestamp (str): The time at which the action was performed.
        """
        self.user_data[user_id].append({'action': action, 'timestamp': timestamp})

    def get_user_actions(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieves a list of actions performed by a specified user.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing the user's actions and timestamps.
        """
        return self.user_data.get(user_id, [])

    def get_all_user_actions(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieves all recorded actions for all users.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary mapping user IDs to their actions.
        """
        return dict(self.user_data)

    def analyze_behavior(self, user_id: str) -> Dict[str, Any]:
        """
        Analyzes the actions of a specified user to derive insights.

        Args:
            user_id (str): The unique identifier of the user.

        Returns:
            Dict[str, Any]: A summary of user behavior including total actions and last action timestamp.
        """
        actions = self.get_user_actions(user_id)
        total_actions = len(actions)
        last_action_time = actions[-1]['timestamp'] if actions else None
        return {
            'total_actions': total_actions,
            'last_action_time': last_action_time
        }

# Sample Usage
if __name__ == "__main__":
    tracker = UserBehaviorTracker()
    tracker.add_user_action("user_1", "login", "2023-10-01T10:00:00")
    tracker.add_user_action("user_1", "view_page", "2023-10-01T10:05:00")
    tracker.add_user_action("user_2", "logout", "2023-10-01T10:10:00")

    print(tracker.get_user_actions("user_1"))
    print(tracker.get_all_user_actions())
    print(tracker.analyze_behavior("user_1"))