# -*- coding: utf-8 -*-
# 装饰器


def now():
    print('2015-11-10')


f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)


# 现在，假设我们要增强now()函数的功能，
# 比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2016-11-10')


now()


def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()
print("now.__name__", now.__name__)

import functools


# 返回的是func.__name__  不是wrapper.__name__
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2016-11-10')


now()
print("now.__name__", now.__name__)


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2016-11-10')


now()
print("now.__name__", now.__name__)
