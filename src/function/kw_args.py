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


person('Jack', 24, 'Beijing', 'Engineer')
