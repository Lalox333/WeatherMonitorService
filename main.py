from core.domains.weather import Weather

def run():
    weather = Weather(location="Berlin",temperature_celsius=29,rain_chance=85)
    print(weather.is_freezing(),weather.need_umbrella())




if __name__ == "__main__":
    run()