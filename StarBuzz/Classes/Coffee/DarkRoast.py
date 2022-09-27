#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    DarkRoast
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:51
from Classes.Abstract.Beverage import Beverage


class DarkRoast(Beverage):
    def __init__(self):
        self.description = "Dark Roast Coffee"

    def cost(self) -> float:
        return .99
