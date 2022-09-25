from abc import abstractmethod


class Observer:
    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        raise NotImplementedError

