from core.domains.location import Location
from core.protocols.messenger_protocol import MessengerProtocol
from service.weather_service import WeatherService
import logging
logger = logging.getLogger(__name__)

class WeatherNotificationService:

    def __init__(self, messenger: MessengerProtocol, weather_service: WeatherService):
        self.messenger: MessengerProtocol = messenger
        self.weather_service: WeatherService = weather_service

    def run(self, location: Location):
        try:
            logger.info(f"Sending weather notification for {location.name}")
            summary = self.weather_service.get_weather_summary(location=location)
            self.messenger.send_message(summary)
            logger.info("Weather notification sent successfully")
        except Exception:
            logger.error("Notification failed",exc_info=True)
            raise
