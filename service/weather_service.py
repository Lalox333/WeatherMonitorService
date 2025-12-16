from core.domains.location import Location
from infrastructure.weather_api_client import WeatherApiClient
import logging

logger = logging.getLogger(__name__)


class WeatherService:

    def __init__(self, weather_api_client: WeatherApiClient):
        self.weather_api_client: WeatherApiClient = weather_api_client

    def get_today_weather(self, location: Location):
        return self.weather_api_client.get_weather(location=location)

    def should_take_umbrella(self, location: Location) -> bool:
        return self.weather_api_client.get_weather(location=location).rain_chance > 80

    def is_today_freezing(self, location: Location) -> bool:
        return self.weather_api_client.get_weather(location=location).is_freezing()

    def get_weather_summary(self, location: Location) -> str:
        logger.info(f"Building weather summary for location {location.name}")
        client = self.weather_api_client.get_weather(location=location)
        logger.info("Weather summary built successfully")
        return f"In {location.name} sind es {client.temperature_celsius} Grad und {client.rain_chance} Prozent Regenwahrscheinlichkeit"

