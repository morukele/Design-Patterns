from Interfaces.Observer import Observer
from Interfaces.DisplayElement import DisplayElement
from Classes.WeatherData import WeatherData


class CurrentConditionsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self.humidity = None
        self.temperature = None
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self):
        self.temperature = self.weatherData.getTemperature()
        self.humidity = self.weatherData.getHumidity()
        self.display()

    def display(self):
        print("Current Conditions: " + str(self.temperature) + "F degrees and "
              + str(self.humidity) + "% humidity")
