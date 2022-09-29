#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    NYStylePizza
# @Author:      Oghenemarho ORUKELE
# @Time:        29/09/2022 11:03
from Classes.Abstract.Pizza import Pizza


class NYStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "NY Style Sauce and Cheese Pizza"
        self.dough = "Thin Crust Dough"
        self.sauce = "Marinara Sauce"
        self.toppings.append("Grated Reggiano Cheese")
