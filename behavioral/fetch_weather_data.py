import json
import requests

class WeatherFetcher:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = 'http://api.openweathermap.org/data/2.5/weather'

    def fetch_weather(self, city):
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.base_url, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    def display_weather(self, city):
        weather_data = self.fetch_weather(city)
        if weather_data:
            print(f"Weather in {city}:")
            print(f"Temperature: {weather_data['main']['temp']}°C")
            print(f"Condition: {weather_data['weather'][0]['description']}")
        else:
            print(f"Could not retrieve weather data for {city}.")

if __name__ == '__main__':
    api_key = 'your_api_key_here'
    fetcher = WeatherFetcher(api_key)
    fetcher.display_weather('London')