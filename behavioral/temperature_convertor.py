# behavioral/temperature_converter.py

class TemperatureConverter:
    """
    A class to perform temperature conversion between Celsius, Fahrenheit, and Kelvin.
    """

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """
        Convert Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature converted to Fahrenheit.
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """
        Convert Fahrenheit to Celsius.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature converted to Celsius.
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """
        Convert Celsius to Kelvin.

        Args:
            celsius (float): Temperature in Celsius.

        Returns:
            float: Temperature converted to Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """
        Convert Kelvin to Celsius.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature converted to Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """
        Convert Fahrenheit to Kelvin.

        Args:
            fahrenheit (float): Temperature in Fahrenheit.

        Returns:
            float: Temperature converted to Kelvin.
        """
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """
        Convert Kelvin to Fahrenheit.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature converted to Fahrenheit.
        """
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)


# Sample usage
if __name__ == "__main__":
    temp_in_celsius = 25
    temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
    temp_in_kelvin = TemperatureConverter.celsius_to_kelvin(temp_in_celsius)

    print(f"{temp_in_celsius} °C is {temp_in_fahrenheit:.2f} °F")
    print(f"{temp_in_celsius} °C is {temp_in_kelvin:.2f} K")