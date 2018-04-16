# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name):
        self.name = name


s = Student('Bob')
s.score = 90

print(s.name, s.score)


class Student(object):
    name = 'Student'


s = Student()

print(s.name)

s.name = 'Michael'

print(s.name)
print(Student.name)

del (s.name)
print(s.name)
