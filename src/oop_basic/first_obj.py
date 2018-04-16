# -*- coding: utf-8 -*-


std1 = {'name': 'Michael', 'score': 98}
std2 = {'name': 'Bob', 'score': 81}

print(std1)

print()


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)


class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


print()
bart = Student('Bart Simpson', 59)
lisa = Student('Lisa Simpson', 87)
bart.print_score()
lisa.print_score()

print()

bart.name = 'asdf09'
bart.print_score()


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'


lisa = Student('Lisa', 99)
bart = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart.name, bart.get_grade())
