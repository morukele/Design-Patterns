from abc import abstractmethod
from Interfaces.Observer import Observer


class Subject:
    @abstractmethod
    def registerObserver(self, o: Observer):
        raise NotImplementedError

    def removeObserver(self, o: Observer):
        raise NotImplementedError

    def notifyObservers(self):
        raise NotImplementedError

