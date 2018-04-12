# -*- coding: utf-8 -*-

s = int('11111')
print(s)
s = int('11111', base=3)
print(s)


def int2(x, base=2):
    return int(x, base)


s = int2('100')
print(s)
print()

# functools.partial就是帮助我们创建一个偏函数的

import functools

int2 = functools.partial(int, base=2)
s = int2('111101001')
print(s)
print()

max2 = functools.partial(max, 10)
s = max2(5, 6, 7)
print(s)

max2 = functools.partial(max, 1)
s = max2(5, 6, 7)
print(s)
