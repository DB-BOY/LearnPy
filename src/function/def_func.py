# -*- coding: utf-8 -*-
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-11))


# 空函数
def nop():
    pass


age = 0

if age >= 18:
    pass


# 参数检查

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad Operand type')
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(2))


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.cos(angle)
    return nx, ny


x, y = move(100, 50, 60, math.pi / 6)

print(x, y)

r = move(100, 50, 60, math.pi / 6)
print(r)


# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
#
def quadratic(a, b, c):
    if not isinstance(a, (int, float)):
        raise TypeError('a is not a number')
    if not isinstance(b, (int, float)):
        raise TypeError('b is not a number')
    if not isinstance(c, (int, float)):
        raise TypeError('c is not a number')

    d = b * b - 4 * a * c

    if a == 0:
        if b == 0:
            if c == 0:
                return '无实根'
            else:
                return '无根'
        else:
            x1 = -c / b
            x2 = x1
            return x1, x2
    else:
        if d < 0:
            return '无根'
        else:
            x1 = (-b + math.sqrt(d)) / 2 / a
            x2 = (-b - math.sqrt(d)) / 2 / a
            return x1, x2


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
