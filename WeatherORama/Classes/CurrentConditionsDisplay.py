from Interfaces.Observer import Observer
from Interfaces.DisplayElement import DisplayElement
from Classes.WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self.humidity = None
        self.temperature = None
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.display()

    def display(self):
        print("Current Conditions: " + str(self.temperature) + "F degrees and "
              + str(self.humidity) + "% humidity")
