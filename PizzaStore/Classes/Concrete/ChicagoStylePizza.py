#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    ChicagoStylePizza
# @Author:      Oghenemarho ORUKELE
# @Time:        29/09/2022 11:03
from Classes.Abstract.Pizza import Pizza


class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = "Chicago Style Deep Dish Cheese Pizza"
        self.dough = "Extra Thick Crust Dough"
        self.sauce = "Plum Tomato Sauce"

        self.toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza in square slices")
