# -*- coding: utf-8 -*-

# 请将本地一个文本文件读为一个str并打印出来：
fpath = r'/Users/pro/Python/LearnPy/src/base/base.py'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)
