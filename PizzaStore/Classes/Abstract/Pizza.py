#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    Pizza
# @Author:      Oghenemarho ORUKELE
# @Time:        28/09/2022 14:58
import abc


class Pizza:
    @abc.abstractmethod
    def prepare(self):
        raise NotImplementedError

    @abc.abstractmethod
    def bake(self):
        raise NotImplementedError

    @abc.abstractmethod
    def cut(self):
        raise NotImplementedError

    @abc.abstractmethod
    def box(self):
        raise NotImplementedError