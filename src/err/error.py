# -*- coding: utf-8 -*-


# 没有默认的错误处理机制,需要写的代码
def foo():
    r = some_function()
    if r == (-1):
        return (-1)
    # do something
    return r


def bar():
    r = foo()
    if r == (-1):
        print('Error')
    else:
        pass


# try

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

# eg.2
print('')

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# eg.3
print('')

try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

print('')


def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


print('处理异常-----')


def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


main()

print('未处理异常-----')


def test():
    bar('0')


# test()

print('异常写文件')

import logging


def log_test():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)


# log_test()

# 抛出错误

print('抛出错误')


class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# print(foo('0'))


print('抛出错误---处理')


def foo(s):
    n = int(s)
    if n == 0:
        raise ValueError('invalid value: %s' % s)
    return 10 / n


def bar():
    try:
        foo('0')
    except ValueError as e:
        print('ValueError!')
        raise


# bar()


# print(int('7.6'))

from functools import reduce


def str2num(s):
    try:
        x = int(s)
    except ValueError as e:
        x = float(s)
    finally:
        return x


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')
    print('99 + 88 + 7.6 =', r)


main()
