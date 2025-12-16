import requests
import os
from datetime import datetime
from core.domains.location import Location
from core.domains.weather import Weather


class WeatherApiClient:

    def get_weather(self,location:Location):

        BASE_URL = "https://api.open-meteo.com/v1/forecast"
        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "hourly": ["temperature_2m", "precipitation_probability"],
            "timezone": "Europe/Berlin",
            "forecast_days": 1,
        }

        response = requests.get(url=BASE_URL, params=params)
        response.raise_for_status()
        data =  response.json()

        current_hour = datetime.now().hour
        hourly = data["hourly"]

        actual_weather_time = [time for time in hourly["time"] if int(time.split("T")[1].split(":")[0]) == int(current_hour)]
        time_index = hourly["time"].index(actual_weather_time[0])

        temp = hourly["temperature_2m"][time_index]
        rain = hourly["precipitation_probability"][time_index]

        return Weather(
            location=location.name,
            temperature_celsius=temp,
            rain_chance=rain

        )











