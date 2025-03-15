import json
import requests

class WeatherFetcher:
    """Fetches weather data from a public API."""
    API_URL = 'http://api.openweathermap.org/data/2.5/weather'

    def __init__(self, api_key):
        """Initializes WeatherFetcher with API key."""
        self.api_key = api_key

    def fetch_weather(self, city):
        """Fetches weather data for a given city."""
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}
        response = requests.get(self.API_URL, params=params)
        return self._handle_response(response)

    def _handle_response(self, response):
        """Handles the API response and returns relevant data."""
        if response.status_code == 200:
            data = response.json()
            return {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description']
            }
        else:
            return {'error': response.json().get('message', 'Error fetching data')}

if __name__ == '__main__':
    api_key = 'YOUR_API_KEY'
    fetcher = WeatherFetcher(api_key)
    city = 'London'
    weather_data = fetcher.fetch_weather(city)
    print(json.dumps(weather_data, indent=4))