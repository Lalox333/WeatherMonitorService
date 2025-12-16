from core.config.settings import Settings
from core.domains.location import Location
from infrastructure.messengers.telegram_messenger import TelegramMessenger
from infrastructure.weather_api_client import WeatherApiClient
from service.weather_notification_service import WeatherNotificationService
from service.weather_service import WeatherService
from core.logging_setup import setup_logging


def run():
    settings = Settings()

    setup_logging()
    location = Location(name=settings.location_name, latitude=settings.latitude, longitude=settings.longitude)
    weather_client = WeatherApiClient()
    weather_service = WeatherService(weather_client)
    messenger = TelegramMessenger(chat_id=settings.telegram_chat_id, api_token=settings.telegram_api_token)
    notification_service = WeatherNotificationService(messenger=messenger, weather_service=weather_service)
    notification_service.run(location=location)


if __name__ == "__main__":
    run()
