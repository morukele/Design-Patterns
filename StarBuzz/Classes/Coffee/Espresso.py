#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Espresso
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:44
from Classes.Abstract.Beverage import Beverage


class Espresso(Beverage):
    def __init__(self):
        self.description = "Espresso"

    def cost(self) -> float:
        return 1.99
