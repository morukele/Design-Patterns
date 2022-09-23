from Classes.Ducks.MallardDuck import MallardDuck
from Classes.Ducks.ModelDuck import ModelDuck
from Classes.Devices.DuckCall import DuckCall
from Classes.SuperClasses.Duck import Duck
from Classes.Traits.FlyRocketPowered import FlyRocketPowered


def main():
    mallard: Duck = MallardDuck()
    mallard.performQuack()
    mallard.performFly()

    model: Duck = ModelDuck()
    model.performFly()
    model.setFlyBehaviour(FlyRocketPowered())
    model.performFly()

    duck_call = DuckCall()
    duck_call.quack()


if __name__ == "__main__":
    main()
