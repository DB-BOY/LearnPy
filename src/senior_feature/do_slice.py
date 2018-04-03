# -*- coding: utf-8 -*-

# 切片操作符 slice
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L)
print()

print(L[0], L[1], L[2])

print(L[:3])
print(L[1:3])
print(L[-1:])

L = list(range(100))
print(L)
print()

print(L[:10])
print(L[-10:])
print(L[10:20])
print(L[:10:2])
print(L[::5])

# tuple
t = (0, 1, 2, 3, 4, 5)
print(t)
print()
print(t[:3])
print(t[::2])

t = 'abcdefg'
print(t)
print()
print(t[:3])
print(t[::2])
