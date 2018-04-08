# -*- coding: utf-8 -*-
# Higher-order function
# 编写高阶函数，就是让函数的参数能够接收别的函数。

# 变量指向函数
print(abs(-10))

print(abs)

f = abs
print(f(-10))


# 当abs指向变量时,abs()已经不能使用了,必须通过导入模块,使用模块.abs()方式实现
# abs = 10
# print(abs(-10))
#
# import builtins
# builtins.abs(-10)


# 传入函数


def add(x, y, f):
    return f(x) + f(y)


print(add(30, 8, abs))
