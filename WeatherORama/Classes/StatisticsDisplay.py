from Interfaces.Observer import Observer
from Interfaces.DisplayElement import DisplayElement
from Classes.WeatherData import WeatherData


class StatisticsDisplay(Observer, DisplayElement):
    def __init__(self, weatherData: WeatherData):
        self.minTemp = 200.00
        self.maxTemp = float()
        self.numReadings = int()
        self.tempSum = float()
        self.weatherData = weatherData
        self.weatherData.registerObserver(self)

    def update(self):
        temp = self.weatherData.getTemperature()
        self.tempSum += temp
        self.numReadings += 1

        if temp > self.maxTemp:
            self.maxTemp = temp

        if temp < self.minTemp:
            self.minTemp = temp

        self.display()

    def display(self):
        print("Avg/Max/Min temperature = " + str(float(self.tempSum/self.numReadings))
              + "/" + str(float(self.maxTemp)) + "/" + str(self.minTemp))
