# -*- coding: utf-8 -*-
import os
import pickle

'序列化'
d = dict(name='bob', age=20, score=88)

p = pickle.dumps(d)
print(p)

with open(os.path.join(os.path.abspath('.'), 'dump.txt'), 'wb') as f:
    pickle.dump(d, f)

with open(os.path.join(os.path.abspath('.'), 'dump.txt'), 'rb') as f:
    d = pickle.load(f)
    print(d)

# json


# JSON类型	    Python类型
# {}      	    dict
# []	        list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None
print()
print('------json操作')

import json

j = json.dumps(d)
print(j)

j2d = json.loads(j)
print(j2d)


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)


# jsond = json.dumps(s)
# print(jsond)

# 对象不能直接转为json
# 1.需要处理
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


# 2. 把class 变为dict
print(' 2. 把class 变为dic')
print(json.dumps(s, default=lambda obj: obj.__dict__))


# 定义了__slots__的class, 不能用上面的方法
# 定义hook方法转换
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


json_str = '{"age": 20, "score": 88, "name": "Bob"}'
j = json.loads(json_str, object_hook=dict2student)
print(j)
