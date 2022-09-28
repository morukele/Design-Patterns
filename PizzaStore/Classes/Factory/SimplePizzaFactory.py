#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    SimplePizzaFactory
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 15:06
from Classes.Concrete.Pizza import Pizza, PepperoniPizza, ClamPizza, CheesePizza, VeggiePizza


class SimplePizzaFactory:
    def __init__(self):
        self.pizza: Pizza = None

    def createPizza(self, pizzaType: str) -> Pizza:
        if pizzaType.__eq__("cheese"):
            self.pizza = CheesePizza()
        elif pizzaType.__eq__("pepperoni"):
            self.pizza = PepperoniPizza()
        elif pizzaType.__eq__("clam"):
            self.pizza = ClamPizza()
        elif pizzaType.__eq__("veggie"):
            self.pizza = VeggiePizza()

        return self.pizza
