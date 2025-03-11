import json
import os
from datetime import datetime

def log_event(event_type, message):
    log_entry = {
        'timestamp': datetime.now().isoformat(),
        'event_type': event_type,
        'message': message
    }
    log_file = 'events_log.json'
    if os.path.exists(log_file):
        with open(log_file, 'r') as file:
            logs = json.load(file)
    else:
        logs = []
    logs.append(log_entry)
    with open(log_file, 'w') as file:
        json.dump(logs, file, indent=4)

if __name__ == '__main__':
    log_event('INFO', 'Application started')
    log_event('ERROR', 'An error occurred')
    log_event('INFO', 'Application finished')
    with open('events_log.json', 'r') as file:
        print(json.load(file))