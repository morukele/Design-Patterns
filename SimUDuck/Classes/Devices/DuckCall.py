from Classes.Traits.Quack import Quack


class DuckCall:
    def __init__(self):
        self.quackBehaviour = Quack()

    def quack(self):
        self.quackBehaviour.quack()
