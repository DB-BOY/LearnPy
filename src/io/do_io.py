# -*- coding: utf-8 -*-

f = open('/Users/pro/Python/LearnPy/src/io/test.txt', 'r')

# filenotfounderror
# f = open('/Users/pro/Python/LearnPy/src/io/test1.txt', 'r')
read = f.read()
f.close()

print(read)

print()

try:
    f = open('/path/to/file', 'r')
    print(f.read())
except FileNotFoundError as e:
    print("except:", e)
finally:
    if f:
        f.close()

# Python引入了with语句来自动帮我们调用close()
print('Python引入了with语句来自动帮我们调用close()')
with open('/Users/pro/Python/LearnPy/src/io/test.txt', 'r') as f:
    print(f.read())

print('----readlines()')

with open('/Users/pro/Python/LearnPy/src/io/test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())

# file-like object
print('=====file-like object')
f = open('/Users/pro/Python/LearnPy/src/io/test.jpg', 'rb')
ff = f.read()
f.close()
print('jpg:')
print(ff)

print('--gbk编码:')

with open('/Users/pro/Python/LearnPy/src/io/test.txt', 'r', encoding='gbk') as f:
    print(f.read())

print('--gbk编码:  不规范的用error 处理')
with open('/Users/pro/Python/LearnPy/src/io/test.txt', 'r', encoding='gbk', errors='ignore') as f:
    print(f.read())

print('-=-=-=-=-=-write()')
print('以"w"模式写入文件时，如果文件已存在，会直接覆盖')
f = open('/Users/pro/Python/LearnPy/src/io/test.txt', 'w')
f.write('helloworld')
f.close()

f = open('/Users/pro/Python/LearnPy/src/io/test.txt', 'a')
f.write('helloworld')
f.close()
# print(f)
