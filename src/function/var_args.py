# -*- coding: utf-8 -*-

def power(x):
    return x * x


print(power(5))


def power(x, n=2):
    if not isinstance(x, (int, float)):
        raise TypeError('x is not a number')
    if not isinstance(n, (int, float)):
        raise TypeError('n is not a number')
    s = 1
    while n > 0:
        n = n - 1
        s = s * x

    return s


print(power(5, 2))


def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)


enroll('Sarah', 'F')

print()


def enroll(name, gender, age=6, city='Beijing'):
    print('name:', name)
    print('gender:', gender)
    print('age:', age)
    print('city:', city)


enroll('Sarah', 'F')
enroll('Bob', 'M', 7)
enroll('Adam', 'M', city='Tianjin')

print()


def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())


# 定义默认参数要牢记一点：默认参数必须指向不变对象！

def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


# 可变参数
# 在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，
# 可以是1个、2个到任意个，还可以是0个。
#
# 我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。
#
# 要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，
# 我们首先想到可以把a，b，c……作为一个list或tuple传进来，这样，函数可以定义如下：


def calc(numbers):
    sum = 0

    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))


# 我们把函数的参数改为可变参数：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 2, 3))

nums = [1, 2, 3]
print(calc(nums[0], nums[1], nums[2]))

print(calc(*nums))
