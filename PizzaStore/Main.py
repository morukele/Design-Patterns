#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Main
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 14:37
from Client.PizzaStore import PizzaStore
from Classes.Factory.SimplePizzaFactory import SimplePizzaFactory

def main():
    factory = SimplePizzaFactory()
    pizzaStore = PizzaStore(factory)
    pizzaStore.orderPizza("cheese")
    print("--------- Next Order ---------")
    pizzaStore.orderPizza("veggie")


if __name__ == "__main__":
    main()
