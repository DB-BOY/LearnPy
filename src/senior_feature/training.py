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

print()


def findMinAndMax(L):
    if not isinstance(L, Iterable):
        print('类型错误')
        return L
    min = None
    max = None

    print(L)
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

# 如果list中既包含字符串，又包含整数，由于非字符串类型没有lower()方法，所以列表生成式会报错：


L = ['Hello', 'World', 18, 'Apple', None]

L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')

print()
print("杨辉三角:")


## -*- coding: utf-8 -*-

def triangles():
    L = [1]
    while True:
        yield L
        L = [1] + [L[i] + L[i + 1] for i in range(len(L) - 1)] + [1]


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
