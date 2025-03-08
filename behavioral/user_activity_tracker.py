# behavioral/user_activity.py

from datetime import datetime, timedelta
from collections import defaultdict

class UserActivityTracker:
    """A class to track user activity including login and logout timestamps."""

    def __init__(self):
        """Initializes an empty activity log."""
        self.activity_log = defaultdict(list)

    def log_login(self, user_id: str):
        """
        Logs the login time for a user.

        Parameters:
            user_id (str): The ID of the user logging in.
        """
        self.activity_log[user_id].append(('login', datetime.now()))

    def log_logout(self, user_id: str):
        """
        Logs the logout time for a user.

        Parameters:
            user_id (str): The ID of the user logging out.
        """
        self.activity_log[user_id].append(('logout', datetime.now()))

    def get_user_activity(self, user_id: str, hours: int = 24):
        """
        Retrieves user activity for the specified duration.

        Parameters:
            user_id (str): The ID of the user whose activity is retrieved.
            hours (int): The number of hours back from now to check for activity.

        Returns:
            List[Tuple[str, datetime]]: List of login/logout activities within the time frame.
        """
        end_time = datetime.now()
        start_time = end_time - timedelta(hours=hours)
        activities = [
            activity for activity in self.activity_log[user_id]
            if start_time <= activity[1] <= end_time
        ]
        return activities

# Sample usage
if __name__ == "__main__":
    tracker = UserActivityTracker()
    tracker.log_login("user_1")
    tracker.log_logout("user_1")
    
    # Simulate some delay
    import time
    time.sleep(2)
    
    tracker.log_login("user_1")
    
    # Retrieve activities in the last hour
    activities = tracker.get_user_activity("user_1", hours=1)
    for activity in activities:
        print(f"Activity: {activity[0]}, Time: {activity[1]}")