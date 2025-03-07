python
class UserBehavior:
    def __init__(self, user_id):
        self.user_id = user_id
        self.action_log = []

    def log_action(self, action):
        self.action_log.append(action)

    def get_action_history(self):
        return self.action_log

    def clear_history(self):
        self.action_log.clear()

    def most_common_action(self):
        if not self.action_log:
            return None
        return max(set(self.action_log), key=self.action_log.count)