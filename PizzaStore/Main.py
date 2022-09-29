#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Main
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 14:37
from Classes.Abstract.PizzaStore import PizzaStore
from Client.ChicagoPizzaStore import ChicagoPizzaStore
from Client.NYPizzaStore import NYPizzaStore


def main():
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.orderPizza("cheese")
    print("Ethan ordered a " + pizza.getName() + "\n")

    pizza = chicagoStore.orderPizza("cheese")
    print("Joel ordered a " + pizza.getName() + "\n")


if __name__ == "__main__":
    main()
