# -*- coding: utf-8 -*-
b = abs(100)
print(b)
b = abs(-10)
print(b)

# b = abs(1,2)
# print(b)

b = max(2, 3)
print(b)
b = max(2, 3, 5, -2)
print(b)

# b = int('a')
# print(b)
b = int('123')
print(b)
# b = int('123.4')
b = int(123.4)
print(b)
b = float('12.34')
print(b)

b = str(12.3)
print(b)
b = str(100)
print(b)

b = bool('1')
print(b)
b = bool('12')
print(b)
b = bool()
print(b)

# 别名
a = abs
print(a(-111))

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
