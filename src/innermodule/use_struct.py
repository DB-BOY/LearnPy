# -*- coding: utf-8 -*-
import struct

s = struct.pack('>I', 10240099)
print(s)
# >表示字节顺序是big-endian，也就是网络序，
# I表示4字节无符号整数
# H表示2字节无符号整数
us = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')
print(us)

# bmp 头信息  前30个字节
# 两个字节：'BM'表示Windows位图, 'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'
up = struct.unpack('<ccIIIIIIHH', s)
print(up)
