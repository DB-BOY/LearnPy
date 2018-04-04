# -*- coding: utf-8 -*-
# 1.凡是可作用于for循环的对象都是Iterable类型；
# 2.凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 3.集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# 4.Python的for循环本质上就是通过不断调用next()函数实现的，

from collections import Iterable, Iterator

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print()
print("可以使用isinstance()判断一个对象是否是Iterator对象")
print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance((x for x in range(10)), Iterator))
print(isinstance(100, Iterator))

print()
print("生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。把list、dict、str等Iterable变成Iterator可以使用iter()函数：")

print(isinstance(iter([]), Iterator))
print(isinstance(iter('abc'), Iterator))

for x in [1, 2, 3, 4, 5]:
    pass

# 实际上完全等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break
