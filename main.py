import os
from infrastructure.weather_api_client import WeatherApiClient
from dotenv import load_dotenv
from core.domains.location import Location


def run():
    load_dotenv()
    location = Location(
        name=os.getenv("LOCATION_NAME"),
        latitude=float(os.getenv("LATITUDE")),
        longitude=float(os.getenv("LONGITUDE"))
    )
    weather_api_client = WeatherApiClient()
    data = weather_api_client.get_weather(location)



if __name__ == "__main__":
    run()