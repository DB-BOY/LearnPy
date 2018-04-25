# -*- coding: utf-8 -*-
import re

s = 'ABC\\-001'

l = re.match(r'^\d{3}\-\d{3,8}$', '010-123450')
print(l)

# 匹配不成功,返回None
l = re.match(r'^\d{3}\-\d{3,8}$', '010-1234500000')
print(l)

test = '123456'

if re.match('^\d*$', test):
    print("ok")
else:
    print("error")

# 切分字符串

s = 'a b   c d'
l = s.split(' ')
print(l)

l = re.split(r'\s+', s)
print(l)

s = 'a,b,c  d e'
l = re.split(r'[\s\,]+', s)
print(l)

s = 'a,b,c ;; d e;f'
l = re.split(r'[\s\,\;]+', s)
print(l)

# 分组
# ^(\d{3})-(\d{3,8})$

m = re.match(r'^(\d{3})-(\d{3,8})$', '010-98765')
print(m)
# print('len(m): ',len(m))
print('m[0]: ', m[0])
print('m.group(0): ', m.group(0))
print('m.group(1): ', m.group(1))
print('m.group(2): ', m.group(2))
print('m.groups: ', m.groups())

t = '19:05:30'
m = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)
print(m)
print(m.groups())

# 日期
# '^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
reg = r'^(0[1-9]|1[0-2]|[0-9])-(0[1-9]|1[0-9]|2[0-9]|3[0-1]|[0-9])$'
t1 = '2-20'
t2 = '2-30'
t3 = '4-31'

m = re.match(reg, t1)
print(m)

m = re.match(reg, t2)
print(m)

m = re.match(reg, t3)
print(m)

# 贪婪匹配

g = re.match(r'^(\d+)(0*)$', '102300').groups()
print(g)

g = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(g)

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

g = re_telephone.match('010-12345').groups()
print(g)
g = re_telephone.match('010-8086').groups()
print(g)
