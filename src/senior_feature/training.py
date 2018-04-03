# -*- coding: utf-8 -*-

# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法
# 利用递归实现, 判断首位是不是有空格

def trim(s):
    if len(s) == 0:
        return s
    elif s[0] == ' ':
        return trim(s[1:])
    elif s[-1] == ' ':
        return trim(s[:-1])
    return s


print(trim('hello  '))
print(trim('  hello'))
print(trim('  hello  '))
print(trim(''))
print(trim('    '))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
    print()

# 请使用迭代查找一个list中最小和最大值，并返回一个tuple：

from collections import Iterable


def findMinAndMax(L):
    if not isinstance(L, Iterable):
        print('类型错误')
        return L
    min = None
    max = None

    print(L)
    print()
    # 拦截空list
    if len(L) == 0:
        return (min, max)
    # 非空操作
    min = max = L[0]
    # print(min, max)
    for i in L:
        if i <= min:
            min = i
        elif i >= max:
            max = i
            # print(min, max)
    return (min, max)


if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
