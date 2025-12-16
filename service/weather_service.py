from core.domains.location import Location
from infrastructure.weather_api_client import WeatherApiClient


class WeatherService:

    def __init__(self, weather_api_client: WeatherApiClient):
        self.weather_api_client: WeatherApiClient = weather_api_client

    def get_today_weather(self, location: Location):
        return self.weather_api_client.get_weather(location=location)
