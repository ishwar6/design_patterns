import random

class BehaviorTracker:
    def __init__(self):
        self.behaviors = {}

    def record_behavior(self, user_id, behavior):
        if user_id not in self.behaviors:
            self.behaviors[user_id] = []
        self.behaviors[user_id].append(behavior)

    def get_behavior_summary(self, user_id):
        if user_id not in self.behaviors:
            return None
        return {
            "total_behaviors": len(self.behaviors[user_id]),
            "unique_behaviors": len(set(self.behaviors[user_id])),
            "behavior_counts": {behavior: self.behaviors[user_id].count(behavior) for behavior in set(self.behaviors[user_id])}
        }

    def randomly_trigger_behavior(self, user_id):
        actions = ["viewed", "clicked", "liked", "shared"]
        behavior = random.choice(actions)
        self.record_behavior(user_id, behavior)
        return behavior

tracker = BehaviorTracker()

for _ in range(10):
    user_id = f"user_{random.randint(1, 5)}"
    triggered_behavior = tracker.randomly_trigger_behavior(user_id)
    print(f"{user_id} {triggered_behavior}")

for user_id in [f"user_{i}" for i in range(1, 6)]:
    summary = tracker.get_behavior_summary(user_id)
    print(f"Summary for {user_id}: {summary}")