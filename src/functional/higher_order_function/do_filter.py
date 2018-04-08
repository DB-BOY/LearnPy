# -*- coding: utf-8 -*-
# 与map相同,作用于数组中每个数
# 与map不同, 根据返回值true/false, 决定保留还是放弃该元素



def is_odd(n):
    return n % 2 == 1


l = filter(is_odd, [1, 2, 4, 5, 6, 7, 8, 9, 94])
print(list(l))


def not_empty(s):
    return s and s.strip()


l = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ', 'C ']))
print(l)

# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，
# 所以要强迫filter()完成计算结果，
# 需要用list()函数获得所有结果并返回list。
