# -*- coding: utf-8 -*-

L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(next(g))
print(next(g))

print()

for n in g:
    print(n)

print()


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


fib(6)

print()


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(4)
for x in f:
    print(x)

print()


def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))

g = fib(6)
while True:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value: ', e.value)
        break

L = [1]
print([0] + L)
print(L + [0])
