#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    CondimentDecorator
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:41
import abc
from Classes.Abstract.Beverage import Beverage


class CondimentDecorator(Beverage):
    beverage = Beverage()

    @abc.abstractmethod
    def getDescription(self) -> str:
        raise NotImplementedError(
            "The getDescription() not implemented in a class that implements CondimentDecorator Class"
        )
