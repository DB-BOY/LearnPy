# -*- coding: utf-8 -*-

from types import MethodType


class Student(object):
    pass


s = Student()

s.name = 'Michael'

print(s.name)


# class Student(object):

def set_age(self, age):  # 定义一个函数作为实例方法
    self.age = age


s = Student()

# 给s对象绑定方法
s.set_age = MethodType(set_age, s)

s.set_age(25)


# 给一个实例绑定的方法，对另一个实例是不起作用的：
# s2 = Student()
# s2.set_age(22)


# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self, score):
    self.score = score


Student.set_score = set_score


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class People(object):
    __slots__ = ('name', 'age')


s = People()
s.name = 'michael'
s.age = 12
# s.gender = 'male'         # slots

print(s)


# slots 绑定的属性,仅对本类有效,子类无效

class GraduateStudent(Student):
    pass


g = GraduateStudent()
g.gender = 'male'

print(g.gender)
