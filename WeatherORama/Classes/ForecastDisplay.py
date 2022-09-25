from Interfaces.Observer import Observer
from Interfaces.DisplayElement import DisplayElement
from Classes.WeatherData import WeatherData


class ForcastDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self.currentPressure = 29.92
        self.lastPressure = float()
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self, temp: float, humidity: float, pressure: float):
        self.lastPressure = self.currentPressure
        self.currentPressure = pressure

        self.display()

    def display(self):
        if self.currentPressure > self.lastPressure:
            print("Forcast: Improving weather on the way!")
        elif self.currentPressure == self.lastPressure:
            print("Forcast: More of the same")
        elif self.currentPressure < self.lastPressure:
            print("Forcast: Watch out for cooler, rainy weather")
