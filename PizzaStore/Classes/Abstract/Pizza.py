#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Pizza
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 14:58
import abc

from typing import List


class Pizza(abc.ABC):
    def __init__(self):
        self.name: str = str()
        self.dough: str = str()
        self.sauce: str = str()
        self.toppings: List[str] = list()

    def prepare(self):
        print("Preparing " + self.name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")

        for topping in self.toppings:
            print(" " + topping)

    @staticmethod
    def bake():
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    @staticmethod
    def box():
        print("Place pizza in official PizzaStore Box")

    def getName(self) -> str:
        return self.name
