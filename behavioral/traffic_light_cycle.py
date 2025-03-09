# behavioral/traffic_light.py

from enum import Enum
import time

class TrafficLightColor(Enum):
    RED = "Red"
    YELLOW = "Yellow"
    GREEN = "Green"

class TrafficLight:
    def __init__(self, duration_red: int, duration_yellow: int, duration_green: int):
        """
        Initializes the TrafficLight with specified signals' durations.

        Args:
            duration_red (int): Duration in seconds for the red light.
            duration_yellow (int): Duration in seconds for the yellow light.
            duration_green (int): Duration in seconds for the green light.
        """
        self.durations = {
            TrafficLightColor.RED: duration_red,
            TrafficLightColor.YELLOW: duration_yellow,
            TrafficLightColor.GREEN: duration_green
        }
        self.current_color = TrafficLightColor.RED

    def switch_light(self):
        """
        Switches the traffic light to the next color in the sequence.
        """
        if self.current_color == TrafficLightColor.RED:
            self.current_color = TrafficLightColor.GREEN
        elif self.current_color == TrafficLightColor.GREEN:
            self.current_color = TrafficLightColor.YELLOW
        else:
            self.current_color = TrafficLightColor.RED

    def run_cycle(self):
        """
        Runs a single cycle of the traffic light, switching through colors.
        """
        while True:
            print(f"Traffic Light is now: {self.current_color.value}")
            time.sleep(self.durations[self.current_color])
            self.switch_light()

def main():
    """
    Main function to demonstrate the TrafficLight functionality.
    Set durations for each color and run the traffic light cycle.
    """
    traffic_light = TrafficLight(duration_red=5, duration_yellow=2, duration_green=4)
    try:
        traffic_light.run_cycle()
    except KeyboardInterrupt:
        print("\nTraffic light simulation stopped.")

if __name__ == "__main__":
    main()