#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    PizzaStore
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 15:07
from Classes.Abstract.Pizza import Pizza
import abc


class PizzaStore:
    def orderPizza(self, pizzaType: str) -> Pizza:
        pizza: Pizza

        pizza = self.createPizza(pizzaType)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abc.abstractmethod
    def createPizza(self, pizzaType: str) -> Pizza:
        pass
