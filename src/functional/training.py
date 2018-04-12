# -*- coding: utf-8 -*-

# 利用闭包返回一个计数器函数，每次调用它返回递增整数：
def createCounter():
    # def f():
    #     x = 0
    #     while True:
    #         x += 1
    #         yield x
    #
    # it = f()

    s = [0]

    def counter():
        s[0] = s[0] + 1
        return s[0]

    return counter


# 测试:

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')


##改造匿名函数
# def is_odd(n):
#     return n % 2 == 1
#
def is_odd(n):
    l = lambda: (n % 2 == 1)
    return l()


L = list(filter(is_odd, range(1, 20)))

print(L)
