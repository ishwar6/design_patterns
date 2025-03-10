# concepts/temperature_converter.py

class TemperatureConverter:
    """A class to convert temperatures between Celsius, Fahrenheit, and Kelvin."""
    
    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit.

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius.

        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.

        Returns:
            float: Temperature in degrees Celsius.
        """
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Convert Celsius to Kelvin.

        Args:
            celsius (float): Temperature in degrees Celsius.

        Returns:
            float: Temperature in Kelvin.
        """
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Convert Kelvin to Celsius.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in degrees Celsius.
        """
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """Convert Fahrenheit to Kelvin.

        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.

        Returns:
            float: Temperature in Kelvin.
        """
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """Convert Kelvin to Fahrenheit.

        Args:
            kelvin (float): Temperature in Kelvin.

        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)


# Sample usage
if __name__ == "__main__":
    celsius_temp = 25.0
    print(f"{celsius_temp}°C is {TemperatureConverter.celsius_to_fahrenheit(celsius_temp)}°F")
    fahrenheit_temp = 77.0
    print(f"{fahrenheit_temp}°F is {TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)}°C")
    kelvin_temp = 298.15
    print(f"{kelvin_temp}K is {TemperatureConverter.kelvin_to_celsius(kelvin_temp)}°C")