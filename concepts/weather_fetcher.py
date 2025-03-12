import json
import requests

class WeatherFetcher:
    """Fetches weather data from an external API."""

    def __init__(self, api_key):
        """Initializes the WeatherFetcher with an API key."""
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def fetch_weather(self, city):
        """Fetches weather data for a given city."""
        parameters = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=parameters)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception('Error fetching data from API')

    def display_weather(self, city):
        """Displays the weather information for a given city."""
        try:
            weather_data = self.fetch_weather(city)
            print(f"City: {weather_data['name']}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Weather: {weather_data['weather'][0]['description']}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    api_key = 'your_api_key_here'
    city_name = 'London'
    weather_fetcher = WeatherFetcher(api_key)
    weather_fetcher.display_weather(city_name)