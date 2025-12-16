from unittest.mock import Mock

from core.domains.location import Location
from core.domains.weather import Weather
from service.weather_service import WeatherService


def test_weather_service():
    location = Location(name="Berlin", longitude=52, latitude=12)
    fake_weather = Weather(
        location=location.name,
        temperature_celsius=29,
        rain_chance=80
    )

    fake_client = Mock()
    fake_client.get_weather.return_value = fake_weather

    service = WeatherService(fake_client)

    result = service.get_today_weather(location=location)

    assert result.temperature_celsius == fake_weather.temperature_celsius
    assert result.rain_chance == fake_weather.rain_chance
    assert result.location == location.name
