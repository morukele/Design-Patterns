#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Mocha
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:55
from Classes.Abstract.CondimentDecorator import CondimentDecorator
from Classes.Abstract.Beverage import Beverage


class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def cost(self) -> float:
        return self.beverage.cost() + .20

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Mocha"
