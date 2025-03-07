python
class UserBehavior:
    def __init__(self, user_id):
        self.user_id = user_id
        self.activities = []

    def log_activity(self, activity_type, timestamp):
        self.activities.append({
            "activity_type": activity_type,
            "timestamp": timestamp
        })

    def get_activity_summary(self):
        summary = {}
        for activity in self.activities:
            activity_type = activity["activity_type"]
            if activity_type not in summary:
                summary[activity_type] = 0
            summary[activity_type] += 1
        return summary

    def clear_activities(self):
        self.activities = []