from dataclasses import dataclass

@dataclass
class Location:

    name:str
    longitude:float
    latitude:float

    def __str__(self):
        return f"Location({self.name})"

    def label(self) -> str:
        return self.name