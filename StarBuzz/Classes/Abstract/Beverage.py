#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Beverage
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:37
import abc
from enum import Enum


class Size(Enum):
    TALL = 1
    GRANDE = 2
    VENTI = 3


class Beverage:
    size: Size = Size.TALL
    description: str = "Unknown Beverage"

    def getDescription(self) -> str:
        return self.description

    def setSize(self, size: Size):
        self.size = size

    def getSize(self) -> Size:
        return self.size

    @abc.abstractmethod
    def cost(self) -> float:
        raise NotImplementedError(
            "The cost() is not implemented in a class that implement Beverage class"
        )
