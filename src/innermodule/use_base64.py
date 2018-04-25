# -*- coding: utf-8 -*-
import base64

b = base64.b64encode(b'binary\x00string')
print("encode: ", b)
d = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
print('decode: ', d)

print('----将  +  /  替换为 -  _ ')
b = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
print('encode: ', b)
b = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
print('safe-encode: ', b)
d = base64.urlsafe_b64decode(b)
print('safe-decode: ', d)
