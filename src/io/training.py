# -*- coding: utf-8 -*-

# 请将本地一个文本文件读为一个str并打印出来：
fpath = r'/Users/pro/Python/LearnPy/src/base/base.py'

with open(fpath, 'r') as f:
    s = f.read()
    print(s)

# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)

print(s)
