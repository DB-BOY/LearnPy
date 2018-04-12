# -*- coding: utf-8 -*-

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    # def f():
    #     x = 0
    #     while True:
    #         x += 1
    #         yield x
    #
    # it = f()

    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]

    return counter


# 测试:

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


##改造匿名函数
# def is_odd(n):
#     return n % 2 == 1
#
def is_odd(n):
    l = lambda: (n % 2 == 1)
    return l()


L = list(filter(is_odd, range(1, 20)))

print(L)
print()
print('请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：')

# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：


import time


def metric(fn):
    def wrapper(*args, **kw):
        t = time.time()
        f = fn(*args, **kw)
        print('%s executed in %s ms' % (fn.__name__, time.time() - t))
        return f

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y;


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z;


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')
else:
    print('测试通过!')


# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call' 的日志。

def log(fn):
    def wrapper(*args, **kw):
        print("begin call ", fn.__name__)
        f = fn(*args, **kw)
        print("end call ", fn.__name__)
        return f

    return wrapper


@log
def show():
    print('show()')


show()

print()


def log(arg):
    def decorator(func=arg):
        text = '' if func == arg else arg

        def wrapper(*args, **kw):
            if text.strip() != '':
                print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator() if callable(arg) else decorator


def log(text):
    def decoraor(fun):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, fun.__name__))
            return fun(*args, **kw)

        return wrapper

    if isinstance(text, str):
        return decoraor
    fun = text
    text = ''
    return decoraor(fun)


@log
def show():
    print('show()')


show()

print()


@log('ddd')
def show():
    print('show()')


show()
