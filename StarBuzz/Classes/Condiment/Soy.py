#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Soy
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 16:00
from Classes.Abstract.Beverage import Beverage, Size
from Classes.Abstract.CondimentDecorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Soy"

    def cost(self) -> float:
        cost: float = self.beverage.cost()
        if self.beverage.getSize() == Size.TALL:
            cost += .10
        elif self.beverage.getSize() == Size.GRANDE:
            cost += .15
        elif self.beverage.getSize() == Size.VENTI:
            cost += .20
        return cost
