# -*- coding: utf-8 -*-
# 匿名

l = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(l)

l = lambda x: x * x
print(l)


def build(x, y):
    return lambda: x * x + y * y


l = build(3, 3)
print(l())
