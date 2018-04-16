# -*- coding: utf-8 -*-
t = type(123)
print(t)

t = type('str')

print(t)

t = type(None)
print(t)

t = type(abs)
print(t)

t = type(123) == type(456)

print(t)
t = type(123) == int
print(t)
t = type('abc') == type('123')
print(t)

t = type('abc') == str

print(t)
t = type('abc') == type(123)
print(t)

import types


def fn():
    pass


print(type(fn))
print(type(fn) == types.FunctionType)

print(type(abs))
print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x: x))
print(type(lambda x: x) == types.LambdaType)

print(type((x for x in range(10))))
print(type((x for x in range(10))) == types.GeneratorType)

# isinstance
# 总是优先使用isinstance()判断类型，可以将指定类型及其子类“一网打尽”。


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，
# 它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：

print(dir('sss'))
print('sss'.__len__())
print(len('sss'))

print()


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))

print('ABC'.lower())


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

x = hasattr(obj, 'x')  # 有属性'x'吗？
print(x)

y = hasattr(obj, 'y')  # 有属性'y'吗？
print(y)

setattr(obj, 'y', 19)  # 设置一个属性'y'

y = hasattr(obj, 'y')  # 有属性'y'吗？
print(y)
print(obj.y)

# z = getattr(obj, 'z') # 获取属性'z'
# print(z)

z = getattr(obj, 'z', 404)  # 获取属性'z'，如果不存在，返回默认值404
print(z)

p = hasattr(obj, 'power')  # 有属性'power'吗？
print(p)

p = getattr(obj, 'power')
print(p)
