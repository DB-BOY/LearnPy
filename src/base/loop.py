# -*- coding: utf-8 -*-

names = ['michael', 'bob', 'tracy']
for name in names:
    print(name)
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

print(list(range(5)))

# 以生成0-100的整数序列，求和

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# 条件退出
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

# 请利用循环依次对list中的每个名字打印出Hello, xxx!
# L = ['Bart', 'Lisa', 'Adam']
L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('hello', name)

# break

n = 1
while n <= 100:
    print(n)
    n = n + 1
print("end")

n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print("end")

# continue

n = 0
while n < 10:
    n = n + 1
    print(n)

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0:
        continue
    print(n)
