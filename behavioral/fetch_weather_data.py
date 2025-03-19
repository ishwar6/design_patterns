import json
import requests

class WeatherFetcher:
    """
    A class to fetch weather data from a public API.
    """
    def __init__(self, api_key, city):
        """
        Initializes the WeatherFetcher with an API key and city name.
        """
        self.api_key = api_key
        self.city = city
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def fetch_weather(self):
        """
        Fetches weather data for the specified city.
        Returns the weather information as a dictionary.
        """
        params = {'q': self.city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {'error': 'City not found or API limit exceeded.'}

    def display_weather(self):
        """
        Fetches and displays the weather data in a readable format.
        """
        weather_data = self.fetch_weather()
        if 'error' in weather_data:
            print(weather_data['error'])
        else:
            print(f"City: {self.city}")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Weather: {weather_data['weather'][0]['description']}")

if __name__ == '__main__':
    api_key = 'your_api_key_here'
    city = 'London'
    weather_fetcher = WeatherFetcher(api_key, city)
    weather_fetcher.display_weather()