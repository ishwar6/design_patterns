# behavior_analysis.py

from collections import defaultdict
from typing import List, Dict

class UserBehaviorAnalyzer:
    """
    A class to analyze user behavior based on interaction logs.
    
    Attributes:
        logs (List[Dict]): A list of dictionaries containing user interaction logs.
    """
    
    def __init__(self, logs: List[Dict[str, str]]):
        """
        Initializes the UserBehaviorAnalyzer with interaction logs.
        
        Args:
            logs (List[Dict[str, str]]): The interaction logs for analysis.
        """
        self.logs = logs

    def analyze_behavior(self) -> Dict[str, Dict[str, int]]:
        """
        Analyzes user behavior from the logs and returns a summary of actions.
        
        Returns:
            Dict[str, Dict[str, int]]: A dictionary where the keys are user IDs
            and the values are dictionaries of action counts.
        """
        user_actions = defaultdict(lambda: defaultdict(int))
        
        for log in self.logs:
            user_id = log.get('user_id')
            action = log.get('action')
            
            if user_id and action:
                user_actions[user_id][action] += 1
                
        return dict(user_actions)

    def most_frequent_action(self) -> Dict[str, str]:
        """
        Determines the most frequent action for each user.

        Returns:
            Dict[str, str]: A dictionary where the keys are user IDs and the
            values are their most frequent actions.
        """
        user_action_counts = self.analyze_behavior()
        most_frequent = {}

        for user_id, actions in user_action_counts.items():
            most_frequent[user_id] = max(actions, key=actions.get)

        return most_frequent


def main():
    sample_logs = [
        {"user_id": "user1", "action": "click"},
        {"user_id": "user1", "action": "view"},
        {"user_id": "user2", "action": "click"},
        {"user_id": "user1", "action": "click"},
        {"user_id": "user2", "action": "view"},
        {"user_id": "user2", "action": "click"},
        {"user_id": "user1", "action": "click"},
        {"user_id": "user3", "action": "view"},
    ]
    
    analyzer = UserBehaviorAnalyzer(sample_logs)
    print("User Behavior Analysis:")
    print(analyzer.analyze_behavior())
    
    print("\nMost Frequent Actions:")
    print(analyzer.most_frequent_action())

if __name__ == "__main__":
    main()