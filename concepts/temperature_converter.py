# concepts/temperature_converter.py

class TemperatureConverter:
    """A class to convert temperatures between Fahrenheit, Celsius, and Kelvin."""

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit: float) -> float:
        """Convert Fahrenheit to Celsius."""
        return (fahrenheit - 32) * 5.0 / 9.0

    @staticmethod
    def celsius_to_fahrenheit(celsius: float) -> float:
        """Convert Celsius to Fahrenheit."""
        return (celsius * 9.0 / 5.0) + 32

    @staticmethod
    def celsius_to_kelvin(celsius: float) -> float:
        """Convert Celsius to Kelvin."""
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin: float) -> float:
        """Convert Kelvin to Celsius."""
        if kelvin < 0:
            raise ValueError("Temperature in Kelvin cannot be negative.")
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit: float) -> float:
        """Convert Fahrenheit to Kelvin."""
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin: float) -> float:
        """Convert Kelvin to Fahrenheit."""
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)


# Sample usage
if __name__ == "__main__":
    fahrenheit_temp = 100.0
    celsius_temp = TemperatureConverter.fahrenheit_to_celsius(fahrenheit_temp)
    kelvin_temp = TemperatureConverter.fahrenheit_to_kelvin(fahrenheit_temp)

    print(f"{fahrenheit_temp}°F is equal to {celsius_temp:.2f}°C.")
    print(f"{fahrenheit_temp}°F is equal to {kelvin_temp:.2f}K.")