from abc import abstractmethod, ABCMeta


class FlyBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass
