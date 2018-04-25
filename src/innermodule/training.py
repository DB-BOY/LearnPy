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


# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')


# base64
# 请写一个能处理去掉=的base64解码函数


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

import base64, struct

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
