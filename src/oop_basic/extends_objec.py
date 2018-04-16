# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()


class Dog(Animal):

    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


print()

dog = Dog()
dog.run()


class Dog(Animal):

    def run(self):
        print('Dog is running...')


class Cat(Animal):

    def run(self):
        print('Cat is running...')


a = list()  # a是list类型
b = Animal()  # b是Animal类型
c = Dog()  # c是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))

b = Animal()
print(isinstance(b, Dog))


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(b)

print()
run_twice(Dog())

print()


class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')


run_twice(Tortoise())

print()
