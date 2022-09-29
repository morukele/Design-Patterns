#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    NYPizzaStore
# @Author:      Oghenemarho ORUKELE
# @Time:        29/09/2022 11:02
from typing import Optional

from Classes.Abstract.Pizza import Pizza
from Classes.Abstract.PizzaStore import PizzaStore
from Classes.Concrete.NYStylePizza import NYStyleCheesePizza


class NYPizzaStore(PizzaStore):
    def createPizza(self, pizzaType: str) -> Optional[Pizza]:
        if pizzaType.__eq__("cheese"):
            return NYStyleCheesePizza()
        else:
            return None
