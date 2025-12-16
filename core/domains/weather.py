from dataclasses import dataclass


@dataclass
class Weather:
    location: str
    temperature_celsius: float
    rain_chance: int

    def need_umbrella(self):
        return self.rain_chance > 80

    def is_freezing(self):
        return self.temperature_celsius <= 0

    