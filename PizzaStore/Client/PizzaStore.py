#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    PizzaStore
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 15:07
from Classes.Abstract.Pizza import Pizza
from Classes.Factory.SimplePizzaFactory import SimplePizzaFactory


class PizzaStore:
    factory: SimplePizzaFactory

    def __init__(self, factory: SimplePizzaFactory):
        self.factory = factory

    def orderPizza(self, pizzaType: str) -> Pizza:
        pizza: Pizza

        pizza = self.factory.createPizza(pizzaType)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
