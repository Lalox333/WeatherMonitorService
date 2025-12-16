from core.domains.weather import Weather

def test_need_umbrella():
    w = Weather(location="Berlin",temperature_celsius=36,rain_chance=85)
    assert w.need_umbrella() == True

    w2 = Weather(location="Berlin",temperature_celsius=-2,rain_chance=12)
    assert w2.need_umbrella() == False


def test_is_freezing():
    w = Weather(location="Berlin",temperature_celsius=-1,rain_chance=95)
    assert w.is_freezing() == True

    w2 = Weather(location="Berlin",temperature_celsius=12,rain_chance=0)
    assert w2.is_freezing() == False

