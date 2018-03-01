# -*- coding: utf-8 -*-
print(r'''hello,\n
world''')

# 数据类型

# 整数
print(100, 1, -8080, 0)

# 浮点型
print(1.23, 3.14, -9.01, 1.23e9, 1.23e-4)

# 字符串
print('abc', 'a', "def")
print("I'm OK")
print('\\\n\\')
print(r'\\\t\\')
print('''line1
... line2
... line3''')

# bool

print(False, True, not True, not False)

a = 100
if a >= 0:
    print(a)
else:
    print(-a)

# 空值

print(None)

# 变量
a = 123
print(a)
a = 'abc'
print(a)
a = True
print(a)

x = 10
x = x + 2
print(x)

# 对象赋值
a = 'ABC'
b = a
a = 'XYZ'
print(b)

# 常量
PI = 3.1415926535
print(PI)

# -----运算
# 除法
print(10 / 3)
print(10 // 3)
print(10 % 3)

print("包含中文")
print(ord('A'))
print(chr(67))
print(ord('中'))
print(chr(25991))

# list
classmates = ['michael', 'bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[1])
print(classmates[-1])

classmates.append('last')
print(classmates)
classmates.insert(1, 'insert')
print(classmates)

L = ['apple', 123, True]
print(L)

s = ['python', 'java', ['asp', 'php'], 'scheme']
print(s)
print(s[2][1])

# tuple  一旦创建不能修改

classmates = ('one', 'two', 'three')
print(classmates)

# condition 条件判断

age = 18
if age >= 18:
    print("your age is ", age)
    print("you are adult")

age = 1
if age >= 18:
    print("your age is ", age)
    print("you are adult")
elif age > 6:
    print("teenager")
else:
    print("kid")
