# -*- coding: utf-8 -*-

d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

# for value in d:
#     print(value)
# dict 迭代的是key ,如果想迭代value 使用 d.values()
# 同时迭代使用 d.items()
print('dict 迭代的是key ,如果想迭代value 使用 d.values()')

for value in d.values():
    print(value)

for key, value in d.items():
    print(key, value)

from collections import Iterable

print(isinstance('aaaaa', Iterable))

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)
