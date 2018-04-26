# -*- coding: utf-8 -*-


import re
from datetime import datetime, timezone, timedelta


# 假设你获取了用户输入的日期和时间如2015-1-21 9:01:30，
# 以及一个时区信息如UTC+5:00，均是str，
# 请编写一个函数将其转换为timestamp：

def to_timestamp(dt_str, tz_str):
    # 字符串转时间
    d = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 正则获取时区
    utc = re.match(r'^UTC([+|-]\d{1,2}):00$', tz_str).group(1)
    # 设置时区,转utc时间
    utc_zone = timezone(timedelta(hours=int(utc)))
    d = d.replace(tzinfo=utc_zone)
    # 返回时间戳
    return d.timestamp()


'''
计算圆周率可以根据公式：
 利用Python提供的itertools模块，我们来计算这个序列的前N项和：
'''


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')

# base64
# 请写一个能处理去掉=的base64解码函数

import base64


def safe_base64_decode(s):
    # 获取字符串长度,判断4的倍数
    size = len(s)
    sum = size % 4
    # 拼接'='
    if size > 0:
        for x in range(4 - sum):
            s = s + b'='

    d = base64.urlsafe_b64decode(s)
    print(d)
    return d


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')

# struct
# 可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。

import struct

bmp_data = base64.b64decode(
    'Qk1oAgAAAAAAADYAAAAoAAAAHAAAAAoAAAABABAAAAAAADICAAASCwAAEgsAAAAAAAAAAAAA/3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9/AHwAfAB8AHwAfAB8AHwAfP9//3//fwB8AHwAfAB8/3//f/9/AHwAfAB8AHz/f/9//3//f/9//38AfAB8AHwAfAB8AHwAfAB8AHz/f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9//3//f/9/AHwAfP9//3//f/9//3//f/9//38AfAB8AHwAfAB8AHwAfP9//3//f/9/AHwAfP9//3//f/9//38AfAB8/3//f/9//3//f/9//3//fwB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8/3//f/9//3//fwB8AHz/f/9//3//f/9//3//f/9/AHwAfP9//3//f/9/AHwAfP9//3//fwB8AHz/f/9/AHz/f/9/AHwAfP9//38AfP9//3//f/9/AHwAfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfP9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9//38AfAB8AHwAfAB8AHwAfAB8/3//f/9/AHwAfAB8AHz/fwB8AHwAfAB8AHwAfAB8AHz/f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//3//f/9//38AAA==')


def bmp_info(data):
    up = struct.unpack('<ccIIIIIIHH', data[:30])
    print(up)
    if up[0] == b'B':
        return {
            'width': up[6],
            'height': up[7],
            'color': up[-1]
        }


bi = bmp_info(bmp_data)
assert bi['width'] == 28
assert bi['height'] == 10
assert bi['color'] == 16
print('ok')

# hashlib

# 存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。
#
# 设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：
import hashlib

print('-----------测试登录')
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}


def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    pw = md5.hexdigest()
    db_pw = db.get(user)
    # print(db_pw)
    # print(pw)
    if db_pw == pw:
        return True
    return False


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

print('-----------测试加盐注册')

# 根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：

db = {}


def register(username, password):
    db[username] = get_md5(password + username + 'the-Salt')


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == get_md5(password + user.salt)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

print('-----------hmac')
import hmac, random


def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'), s.encode('utf-8'), 'MD5').hexdigest()


class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = hmac_md5(self.key, password)


db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}


def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)


# 测试:
assert login('michael', '123456')
assert login('bob', 'abc999')
assert login('alice', 'alice2008')
assert not login('michael', '1234567')
assert not login('bob', '123456')
assert not login('alice', 'Alice2008')
print('ok')

import itertools

# 计算圆周率可以根据公式：
#
# 利用Python提供的itertools模块，我们来计算这个序列的前N项和：

print('计算pi值')


def pi(N):
    ' 计算pi的值 '
    # step 1: 创建一个奇数序列: 1, 3, 5, 7, 9, ...
    natuals = itertools.count(1)
    # step 2: 取该序列的前N项: 1, 3, 5, 7, 9, ..., 2*N-1.
    ns = itertools.takewhile(lambda x: x < N + 1, natuals)
    l = list(ns)
    # step 3: 添加正负符号并用4除: 4/1, -4/3, 4/5, -4/7, 4/9, ...
    for i in range(len(l)):
        l[i] = 2 * l[i] - 1
        if (i % 2 == 1):
            l[i] = 0 - l[i]
        l[i] = 4 / l[i]
    # step 4: 求和:
    return sum(l)


# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')
