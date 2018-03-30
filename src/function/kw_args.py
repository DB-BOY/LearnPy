# -*- coding: utf-8 -*-

# 关键字参数

def person(name, age, **kw):
    print('name', name, 'age', age, 'other', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')

person('Adam', 45, gender='M', job='Engineer')


def person(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name', name, 'age', age, 'other', kw)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


def person(name, age, *, city, job):
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')


def person(name, age, *args, city, job):
    print(name, age, args, city, job)


# person('Jack', 24, 'Beijing', 'Engineer')


def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)


person('Jack', 24, job='Engineer')


def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
