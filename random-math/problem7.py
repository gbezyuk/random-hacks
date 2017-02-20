#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
задачка для 7 класса: в олимпиаде участвовало Х мальчиков и Y математиков,
причем девочек-гуманитариев было столько же, сколько и мальчиков-математиков
сколько человек участвовало в олимпиаде?
"""

"""
each = [(is_boy, is_mathematician)] # e.g (True, False) for a humanitarian boy
total
boys = total - girls
mathematitians = total - humanitarians

count(is_girl, is_humanitarian) == count(is_boy, is_mathematician)

b = X
m = Y
total = T, the point of interest

bm + bh = X         bh = X - bm
bm + gm = Y                                 gm = Y - bm
gm + gh = T - X                             gm = T - X - gh
gh + bh = T - Y     bh = T - Y - gh

                    X - bm = T - Y - gh     Y - bm = T - X - gh

Y - bm = T - X - gh     T = Y + X
gh = bm