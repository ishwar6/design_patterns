import requests
import json

class WeatherFetcher:
    """
    A class to fetch weather data from an external API.
    """

    def __init__(self, api_key):
        """
        Initializes the WeatherFetcher with an API key.
        """
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def fetch_weather(self, city):
        """
        Fetches the weather data for a given city.
        :param city: Name of the city to fetch the weather for.
        :return: A dictionary containing weather data if successful, None otherwise.
        """
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        return None

    def display_weather(self, city):
        """
        Displays the weather information for the specified city.
        :param city: Name of the city to display the weather for.
        """
        weather_data = self.fetch_weather(city)
        if weather_data:
            print(f"Weather in {city}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Conditions: {weather_data['weather'][0]['description']}")
        else:
            print(f"Could not retrieve weather data for {city}.")

if __name__ == '__main__':
    fetcher = WeatherFetcher('your_api_key_here')
    fetcher.display_weather('London')