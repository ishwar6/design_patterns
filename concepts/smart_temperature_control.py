# concepts/smart_temperature_controller.py

class SmartTemperatureController:
    """
    A class to control the temperature of a heating system based on user-defined settings.
    It adjusts the heating based on the current room temperature and the desired temperature,
    providing an efficient way to maintain comfort while saving energy.

    Attributes:
        desired_temperature (float): The target temperature set by the user.
        current_temperature (float): The current detected temperature of the room.
        tolerance (float): Acceptable deviation from the desired temperature.
    """

    def __init__(self, desired_temperature: float, tolerance: float = 0.5):
        """
        Initializes the SmartTemperatureController with desired temperature and tolerance.

        :param desired_temperature: The temperature the user wants to achieve.
        :param tolerance: Tolerance range within which the desired temperature is acceptable.
        """
        self.desired_temperature = desired_temperature
        self.current_temperature = 20.0  # Default initial temperature
        self.tolerance = tolerance

    def update_current_temperature(self, new_temperature: float):
        """
        Updates the current temperature of the room.

        :param new_temperature: The new current temperature to be set.
        """
        self.current_temperature = new_temperature

    def is_heating_needed(self) -> bool:
        """
        Determines if heating is required based on the current and desired temperatures.

        :return: True if heating is needed, False otherwise.
        """
        return self.current_temperature < (self.desired_temperature - self.tolerance)

    def control_heating(self) -> str:
        """
        Controls the heating system based on the current temperature.

        :return: A message indicating whether the heating is ON, OFF, or not required.
        """
        if self.is_heating_needed():
            return "Heating is ON."
        elif self.current_temperature > (self.desired_temperature + self.tolerance):
            return "Heating is OFF."
        else:
            return "Temperature is within acceptable range."

def main():
    """
    Sample usage of the SmartTemperatureController.
    """
    controller = SmartTemperatureController(desired_temperature=22.0)

    # Simulate temperature changes
    temperature_readings = [19.0, 21.5, 22.0, 23.5]

    for reading in temperature_readings:
        controller.update_current_temperature(reading)
        print(f"Current Temperature: {controller.current_temperature}°C - {controller.control_heating()}")

if __name__ == "__main__":
    main()