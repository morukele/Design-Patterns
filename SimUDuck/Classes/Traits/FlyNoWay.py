from Interfaces.FlyBehaviour import FlyBehaviour


class FlyNoWay(FlyBehaviour):
    def fly(self):
        print("I can't fly")