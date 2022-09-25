from Classes.WeatherData import WeatherData
from Classes.CurrentConditionsDisplay import CurrentConditionsDisplay
from Classes.ForecastDisplay import ForcastDisplay
from Classes.StatisticsDisplay import StatisticsDisplay


def main():
    weatherData: WeatherData = WeatherData()

    currentDisplay: CurrentConditionsDisplay = CurrentConditionsDisplay(weatherData)
    statisticsDisplay: StatisticsDisplay = StatisticsDisplay(weatherData)
    forecastDisplay: ForcastDisplay = ForcastDisplay(weatherData)

    weatherData.setMeasurements(80, 65, 30.4)
    weatherData.setMeasurements(82, 70, 29.2)
    weatherData.setMeasurements(78, 90, 29.2)


if __name__ == "__main__":
    main()
