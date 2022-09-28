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
        size: Size = self.beverage.getSize()
        if size == Size.TALL:
            cost += .10
        elif size == Size.GRANDE:
            cost += .15
        elif size == Size.VENTI:
            cost += .20
        return cost
