from abc import abstractmethod
from Interfaces.FlyBehaviour import FlyBehaviour
from Interfaces.QuackBehaviour import QuackBehaviour


class Duck:
    def __init__(self):
        self.flyBehaviour: FlyBehaviour = FlyBehaviour()
        self.quackBehaviour: QuackBehaviour = QuackBehaviour()

    @staticmethod
    def swim():
        print("All ducks float, even decoys!")

    @abstractmethod
    def display(self):
        pass

    def performQuack(self):
        self.quackBehaviour.quack()

    def performFly(self):
        self.flyBehaviour.fly()

    def setFlyBehaviour(self, fb: FlyBehaviour):
        self.flyBehaviour = fb

    def setQuackBehaviour(self, qb: QuackBehaviour):
        self.quackBehaviour = qb
