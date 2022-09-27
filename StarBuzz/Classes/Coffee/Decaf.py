#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Decaf
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:52
from Classes.Abstract.Beverage import Beverage


class Decaf(Beverage):
    def __init__(self):
        self.description = "Decaf Coffee"

    def cost(self) -> float:
        return 1.05
