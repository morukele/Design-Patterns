from Interfaces.Observer import Observer
from Interfaces.DisplayElement import DisplayElement
from Interfaces.Subject import Subject


class HeatIndexDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: Subject):
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)
        self.heatIndex = float()

    def update(self):
        self.heatIndex = 100
        self.display()

    def display(self):
        print("Heat index is " + str(self.heatIndex))