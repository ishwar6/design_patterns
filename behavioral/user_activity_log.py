# behavioral/user_activity_tracker.py

from collections import defaultdict
from datetime import datetime
from typing import List, Dict, Any

class UserActivityTracker:
    """
    A class to track user activity within an application.

    Attributes:
        user_activities (dict): A dictionary that maps user IDs to their activity logs.
    """

    def __init__(self) -> None:
        self.user_activities: Dict[str, List[Dict[str, Any]]] = defaultdict(list)

    def log_activity(self, user_id: str, activity: str) -> None:
        """
        Logs an activity for a given user.

        Args:
            user_id (str): The ID of the user.
            activity (str): A description of the activity performed by the user.
        """
        timestamp = datetime.now().isoformat()
        self.user_activities[user_id].append({"activity": activity, "timestamp": timestamp})

    def get_user_activity(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Retrieves the activity log for a specific user.

        Args:
            user_id (str): The ID of the user whose activities are to be fetched.

        Returns:
            List[Dict[str, Any]]: A list of activities performed by the user.
        """
        return self.user_activities.get(user_id, [])

    def get_all_user_activities(self) -> Dict[str, List[Dict[str, Any]]]:
        """
        Retrieves the activity logs for all users.

        Returns:
            Dict[str, List[Dict[str, Any]]]: A dictionary with user IDs as keys and their activity logs as values.
        """
        return dict(self.user_activities)

# Sample usage of UserActivityTracker

if __name__ == "__main__":
    tracker = UserActivityTracker()

    tracker.log_activity("user1", "Logged in")
    tracker.log_activity("user1", "Viewed dashboard")
    tracker.log_activity("user2", "Signed up")
    tracker.log_activity("user1", "Logged out")

    print("Activity log for user1:")
    print(tracker.get_user_activity("user1"))

    print("\nActivity log for all users:")
    print(tracker.get_all_user_activities())