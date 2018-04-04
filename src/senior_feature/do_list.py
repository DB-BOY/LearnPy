# -*- coding: utf-8 -*-

l = list(range(1, 11))
print(l)

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 替代方案

L = [x * x for x in range(1, 11)]
print(L)

L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

# 导入os模块,列出文件及目录名
import os

L = [d for d in os.listdir('.')]
print(L)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

d = {'x': 'A', 'y': 'B', 'z': 'C'}
L = [k + '=' + v for k, v in d.items()]
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
LL = [s.lower() for s in L]
print(LL)
