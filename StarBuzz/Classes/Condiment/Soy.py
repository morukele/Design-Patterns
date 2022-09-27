#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Soy
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 16:00
from Classes.Abstract.Beverage import Beverage
from Classes.Abstract.CondimentDecorator import CondimentDecorator


class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.beverage = beverage

    def getDescription(self) -> str:
        return self.beverage.getDescription() + ", Soy"

    def cost(self) -> float:
        return self.beverage.cost() + .15
