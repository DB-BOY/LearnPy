# -*- coding: utf-8 -*-

L = sorted([36, 5, -12, 9, -21])
print(L)

L = sorted([36, 5, -12, 9, -21], key=abs)
print(L)

L = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)

print(L)
