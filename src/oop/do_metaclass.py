# -*- coding: utf-8 -*-

from hello import Hello

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

print("用type来定义函数 class等")


# 用type来定义函数 class等

def fn(self, name='world'):  # 先定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn))  # 创建class 类

h = Hello()
h.hello()

print(type(Hello))
print(type(h))

# 要创建一个class对象，type()函数依次传入3个参数：
# Hello = type('Hello', (object,), dict(hello=fn))
# class的名称；
# 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。

print("----metaclass----")


# metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。
# 正常情况下，你不会碰到需要使用metaclass的情况，
# 所以，以下内容看不懂也没关系，因为基本上你不会用到。

# metaclass是类的模板，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)

# L2 = list()
# L2.add(1)


print()
