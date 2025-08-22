def RealSensor():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

# unit test candidate
def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }

def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"

    if readings['temperatureInC'] > 25:
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
        elif readings['precipitation'] >= 60 and readings['windSpeedKMPH'] < 50:
            weather = "Rainy"
    return weather

def testRainy():
    def rainyStub():
        return {
            'temperatureInC': 30,
            'precipitation': 80,
            'humidity': 90,
            'windSpeedKMPH': 45
        }
    weather = report(rainyStub)
    print(weather)
    assert("rain" in weather.lower()), f"Expected 'rain' in weather report, got '{weather}'"

def testHighPrecipitation():
    # This instance of stub needs to be different-
    # to give high precipitation (>60) and low wind-speed (<50)
    def highPrecipLowWindStub():
        return {
            'temperatureInC': 50,
            'precipitation': 70,   # >60
            'humidity': 26,
            'windSpeedKMPH': 40    # <50
        }
    weather = report(highPrecipLowWindStub)
    # strengthen the assert to expose the bug
    # (function returns Sunny day, it should predict rain)
    assert("rain" in weather.lower()), f"Expected 'rain' in weather report, got '{weather}'"

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation()
    print("All is well (maybe!)")
