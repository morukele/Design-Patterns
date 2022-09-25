from typing import List
from Interfaces.Observer import Observer
from Interfaces.Subject import Subject


class WeatherData(Subject):
    def __init__(self):
        self.observers: List[Observer] = list()
        self.temperature: float = float()
        self.humidity: float = float()
        self.pressure: float = float()

    def registerObserver(self, o: Observer):
        self.observers.append(o)

    def removeObserver(self, o: Observer):
        self.observers.remove(o)

    def notifyObservers(self):
        for observer in self.observers:
            observer.update()

    def measurementsChanged(self):
        self.notifyObservers()

    def setMeasurements(self, temperature: float, humidity: float, pressure: float):
        self.temperature = temperature
        self. humidity = humidity
        self. pressure = pressure
        self.measurementsChanged()

    def getTemperature(self):
        return self.temperature

    def getHumidity(self):
        return self.humidity

    def getPressure(self):
        return self.pressure