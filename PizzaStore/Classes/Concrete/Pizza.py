#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Pizza
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 15:02
from Classes.Abstract.Pizza import Pizza


class CheesePizza(Pizza):
    def prepare(self):
        print("Preparing cheese pizza")

    def bake(self):
        print("Baking cheese pizza")

    def cut(self):
        print("Cutting cheese pizza")

    def box(self):
        print("Boxing cheese pizza")


class VeggiePizza(Pizza):
    def prepare(self):
        print("Preparing veggie pizza")

    def bake(self):
        print("Baking veggie pizza")

    def cut(self):
        print("Cutting veggie pizza")

    def box(self):
        print("Boxing veggie pizza")


class ClamPizza(Pizza):
    def prepare(self):
        print("Preparing clam pizza")

    def bake(self):
        print("Baking clam pizza")

    def cut(self):
        print("Cutting clam pizza")

    def box(self):
        print("Boxing clam pizza")


class PepperoniPizza(Pizza):
    def prepare(self):
        print("Preparing pepperoni pizza")

    def bake(self):
        print("Baking pepperoni pizza")

    def cut(self):
        print("Cutting pepperoni pizza")

    def box(self):
        print("Boxing pepperoni pizza")
