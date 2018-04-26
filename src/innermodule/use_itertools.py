# -*- coding: utf-8 -*-

# 无限迭代

import itertools

# count创建一个无线循环的迭代器,一直输出.....
# 参数 表示自然数起点

natuals = itertools.count(1)

for n in natuals:
    if (n > 10):
        break
    print(n)

print("=---------cycle")
# cycle
# 把传入的一个序列无限重复下去

cs = itertools.cycle('abc')

i = 0
for n in cs:
    if (i > 10):
        break
    print(n)
    i = i + 1

print('--------repeat')
# repeat()负责把一个元素无限重复下去，不过如果提供第二个参数就可以限定重复次数

re = itertools.repeat('da', 2)
for n in re:
    print(n)

# takewhile()
print('------- takewhile()')

# 无限循环使用takewhile()截停

natuals = itertools.count(1)

ns = itertools.takewhile(lambda x: x <= 10, natuals)
l = list(ns)
print(l)

# chain()
# 将迭代对象串联
print('------- chain()')

for c in itertools.chain('ABC', 'XYZ'):
    print(c)

# groupby()
# 将相邻的重复元素分组
for key, group in itertools.groupby('aaabbbdddeefeess'):
    print(key, list(group))
#     大小写
print('----大小写')
for key, group in itertools.groupby('AAaaBBbddDeefEess'):
    print(key, list(group))

# 忽略大小写
print('----忽略大小写')
for key, group in itertools.groupby('AAaaBBbddDeefEess', lambda c: c.upper()):
    print(key, list(group))
