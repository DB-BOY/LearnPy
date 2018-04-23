# -*- coding: utf-8 -*-
from io import StringIO

f = StringIO()
x = f.write('eee')
print(x)
x = f.write(' ')
print(x)

print(f.getvalue())

f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

from io import BytesIO

f = BytesIO()
x = f.write('中文'.encode('utf-8'))
print('utf-8', x, f.getvalue())
x = f.write('中文'.encode('gbk'))
print('gbk: ', x, f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')

x = f.read()
print(x)
