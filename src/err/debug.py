# -*- coding: utf-8 -*-
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n


def main():
    foo('0')


# main()

# 改进
# assert
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def main():
    foo('0')


# main()


print('logging')
# logging
import logging

logging.basicConfig(level=logging.INFO)

# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# pdb
print('pdb')
#
# s = '0'
# n = int(s)
# print(10 / n)

# 运行代码，程序会自动在pdb.set_trace()暂停并进入pdb调试环境，
# 可以用命令p查看变量，或者用命令c继续运行：


import pdb

s = '0'
n = int(s)
pdb.set_trace()  # 运行到这里会自动暂停
print(10 / n)
