# file: concepts/temperature_converter.py

class TemperatureConverter:
    """A class to convert temperatures between Celsius, Fahrenheit, and Kelvin."""

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        """Convert temperature from Celsius to Fahrenheit.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
        
        Returns:
            float: Temperature in degrees Fahrenheit.
        """
        if not isinstance(celsius, (int, float)):
            raise ValueError("Input must be an integer or float.")
        return (celsius * 9/5) + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        """Convert temperature from Fahrenheit to Celsius.
        
        Args:
            fahrenheit (float): Temperature in degrees Fahrenheit.
        
        Returns:
            float: Temperature in degrees Celsius.
        """
        if not isinstance(fahrenheit, (int, float)):
            raise ValueError("Input must be an integer or float.")
        return (fahrenheit - 32) * 5/9

    @staticmethod
    def celsius_to_kelvin(celsius):
        """Convert temperature from Celsius to Kelvin.
        
        Args:
            celsius (float): Temperature in degrees Celsius.
        
        Returns:
            float: Temperature in Kelvin.
        """
        if not isinstance(celsius, (int, float)):
            raise ValueError("Input must be an integer or float.")
        return celsius + 273.15

    @staticmethod
    def kelvin_to_celsius(kelvin):
        """Convert temperature from Kelvin to Celsius.
        
        Args:
            kelvin (float): Temperature in Kelvin.
        
        Returns:
            float: Temperature in degrees Celsius.
        """
        if not isinstance(kelvin, (int, float)):
            raise ValueError("Input must be an integer or float.")
        if kelvin < 0:
            raise ValueError("Kelvin cannot be negative.")
        return kelvin - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(fahrenheit):
        """Convert temperature from Fahrenheit to Kelvin.
        
        Args:
            fahrenheit (float): Temperature in Fahrenheit.
        
        Returns:
            float: Temperature in Kelvin.
        """
        celsius = TemperatureConverter.fahrenheit_to_celsius(fahrenheit)
        return TemperatureConverter.celsius_to_kelvin(celsius)

    @staticmethod
    def kelvin_to_fahrenheit(kelvin):
        """Convert temperature from Kelvin to Fahrenheit.
        
        Args:
            kelvin (float): Temperature in Kelvin.
        
        Returns:
            float: Temperature in Fahrenheit.
        """
        celsius = TemperatureConverter.kelvin_to_celsius(kelvin)
        return TemperatureConverter.celsius_to_fahrenheit(celsius)

# Sample Usage
if __name__ == "__main__":
    temp_in_celsius = 25.0
    temp_in_fahrenheit = TemperatureConverter.celsius_to_fahrenheit(temp_in_celsius)
    temp_in_kelvin = TemperatureConverter.celsius_to_kelvin(temp_in_celsius)

    print(f"{temp_in_celsius}°C is equal to {temp_in_fahrenheit}°F")
    print(f"{temp_in_celsius}°C is equal to {temp_in_kelvin}K")