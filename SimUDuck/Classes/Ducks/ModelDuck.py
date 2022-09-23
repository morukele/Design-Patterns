from Classes.SuperClasses.Duck import Duck
from Classes.Traits.FlyNoWay import FlyNoWay
from Classes.Traits.Quack import Quack


class ModelDuck(Duck):
    def __init__(self):
        self.flyBehaviour = FlyNoWay()
        self.quackBehaviour = Quack()

    def display(self):
        print("I am a model duck")
