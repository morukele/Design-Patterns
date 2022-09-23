from abc import abstractmethod, ABCMeta


class QuackBehaviour(metaclass=ABCMeta):
    @abstractmethod
    def quack(self):
        pass
