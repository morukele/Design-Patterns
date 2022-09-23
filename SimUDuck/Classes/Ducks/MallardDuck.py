from ..SuperClasses.Duck import Duck
from ..Traits.FlyWithWings import FlyWithWings
from ..Traits.Quack import Quack


class MallardDuck(Duck):
    def __init__(self):
        self.quackBehaviour = Quack()
        self.flyBehaviour = FlyWithWings()

    def display(self):
        print("I am a real Mallard duck")
