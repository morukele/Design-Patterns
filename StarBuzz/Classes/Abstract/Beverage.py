#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Beverage
# @Author:      Oghenemarho ORUKELE
# @Time:        27/09/2022 15:37
import abc


class Beverage:
    description: str = "Unknown Beverage"

    def getDescription(self) -> str:
        return self.description

    @abc.abstractmethod
    def cost(self) -> float:
        raise NotImplementedError
