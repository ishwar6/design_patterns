python
class BehavioralFeature:
    def __init__(self, user_data):
        self.user_data = user_data

    def analyze_behavior(self):
        return {
            "average_session_time": self.calculate_average_session_time(),
            "most_active_time": self.calculate_most_active_time(),
            "engagement_score": self.calculate_engagement_score(),
        }

    def calculate_average_session_time(self):
        total_time = sum(session['duration'] for session in self.user_data['sessions'])
        return total_time / len(self.user_data['sessions'])

    def calculate_most_active_time(self):
        time_count = {}
        for session in self.user_data['sessions']:
            hour = session['start_time'].hour
            if hour in time_count:
                time_count[hour] += 1
            else:
                time_count[hour] = 1
        return max(time_count, key=time_count.get)

    def calculate_engagement_score(self):
        return (len(self.user_data['interactions']) / 
                len(self.user_data['sessions'])) * 100