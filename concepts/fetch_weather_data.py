import json
import requests

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

    def get_weather(self, city):
        """
        Fetches the weather data for a given city.
        :param city: The name of the city to fetch weather for.
        :return: A dictionary containing weather information.
        """
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f'Error fetching data: {response.status_code}')

    def display_weather(self, city):
        """
        Prints the weather data for a specified city.
        :param city: The name of the city to display weather for.
        """
        try:
            weather_data = self.get_weather(city)
            print(f"Weather in {city}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Description: {weather_data['weather'][0]['description']}")
        except Exception as e:
            print(e)

if __name__ == '__main__':
    api_key = 'your_api_key_here'
    fetcher = WeatherFetcher(api_key)
    fetcher.display_weather('London')