#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Main
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:46
from Classes.Coffee.Espresso import Espresso
from Classes.Coffee.DarkRoast import DarkRoast
from Classes.Condiment.Mocha import Mocha
from Classes.Coffee.HouseBlend import HouseBlend
from Classes.Condiment.Soy import Soy
from Classes.Condiment.Whip import Whip
from Classes.Abstract.Beverage import Size


def main():
    espresso = Espresso()
    print(espresso.getDescription() + " $" + str(espresso.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.getDescription()+ " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3.setSize(Size.GRANDE)
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.getDescription() + " $" + str(beverage3.cost()))


if __name__ == "__main__":
    main()
