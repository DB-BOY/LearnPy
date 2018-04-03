# -*- coding: utf-8 -*-
import time

print(time.time())


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print(fact(1))
print(fact(5))

print(time.time())
print(fact(900))
print(time.time())


# 尾递归
# 尾递归调用时，如果做了优化，栈不会增长，因此，无论多少次调用也不会导致栈溢出
# 但也会导致栈溢出

def fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


print(fact(10))

print(time.time())
print(fact(900))
print(time.time())


# 汉诺塔的递归实现

def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(4, 'A', 'B', 'C')

# move(64, 'A', 'B', 'C')
