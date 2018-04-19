# -*- coding: utf-8 -*-
# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, valuer):
        if not isinstance(valuer, int):
            raise ValueError('score must be an integer')
        if valuer < 0:
            raise ValueError('score must over zero')
        self._width = valuer

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, number):
        if not isinstance(number, int):
            raise ValueError('score must be an integer')
        if number < 0:
            raise ValueError('score must be an zero')
        self._height = number

    @property
    def resolution(self):
        return self._width * self._height


# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')

# enum练习
# 把Student的gender属性改造为枚举类型，可以避免使用字符串：

from enum import Enum, unique


@unique
class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
