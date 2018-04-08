# -*- coding: utf-8 -*-
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
# 输入：['adam', 'LISA', 'barT']，
# 输出：['Adam', 'Lisa', 'Bart']：

from collections import Iterable
from functools import reduce


def normalize(name):
    if len(name) == 0:
        return name
    name = name[0].upper() + name[1:].lower()
    return name


# 测试:
L1 = ['adam', 'LISA', 'barT', '']
L2 = list(map(normalize, L1))
print(L2)


# Python提供的sum()函数可以接受一个list并求和，
# 请编写一个prod()函数，可以接受一个list并利用reduce()求积：
def prod(L):
    if not isinstance(L, Iterable):
        return

    def inner(x, y):
        return x * y

    return reduce(inner, L)


print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 利用map和reduce编写一个str2float函数，
# 把字符串'123.456'转换成浮点数123.456：

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2float(s):
    L = s.split('.')
    x = reduce(lambda x, y: x * 10 + y, map(char2num, L[0]))
    y = 0
    if len(L) > 1:
        y = reduce(lambda x, y: x * 10 + y, map(char2num, L[1]))
        y = y / (10 ** len(L[1]))  # ** 表示 次幂
    return x + y


print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')

print(str2float('123456'))


# 回数是指从左向右读和从右向左读都是一样的数，
# 例如12321，909。请利用filter()筛选出回数：

# 思路, 将数字转为字符串,反转字符串对比
# n = 229
# n_str = str(n)
# print(n_str[::-1])


def is_palindrome(n):
    n_str = str(n)
    return n_str == n_str[::-1]


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')

# 假设我们用一组tuple表示学生名字和成绩：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序：

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

print(L)


def by_name(t):
    return t[0].lower()


L2 = sorted(L, key=by_name)

print(L2)


# 再按成绩从高到低排序：

def by_score(t):
    return t[1]


L2 = sorted(L, key=by_score)

print(L2)
