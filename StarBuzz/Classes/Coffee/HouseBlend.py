#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    HouseBlend
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:48
from Classes.Abstract.Beverage import Beverage


class HouseBlend(Beverage):
    def __init__(self):
        self.description = "House Blend Coffee"

    def cost(self) -> float:
        return .89
