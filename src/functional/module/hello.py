# -*- coding: utf-8 -*-
# 模块
' a test module '
__author__ = 'gin_boy'
import sys


def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world')
    elif len(args) == 2:
        print('hello , %s!' % args[1])
    else:
        print('too many arguments')


if __name__ == '__main__':
    test()

import src.functional.module.web.utils

print()
src.functional.module.web.utils.uweb(['sadfasdfasdfsdf', 'ddddd'])
src.functional.module.web.utils.get('http://www.baidu.com')
src.functional.module.web.utils.greeting('greeting')
src.functional.module.web.utils._private_1('_private_1')
src.functional.module.web.utils._private_2('_private_2')
