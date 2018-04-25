# -*- coding: utf-8 -*-

from datetime import datetime, timedelta, timezone

now = datetime.now()
print(now)
print(type(now))

dt = datetime(2015, 4, 19, 12, 20)  # 用指定日期时间创建datetime
print(dt)

timestamp = dt.timestamp()  # 把datetime转换为timestamp
print(timestamp)

t = datetime.fromtimestamp(timestamp)
print(t)

t = datetime.utcfromtimestamp(timestamp)
print('utc: ', t)

cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
print('str : ', cday)

tz_utc_8 = timezone(timedelta(hours=8))
print('tz_utc_8  : ', tz_utc_8)
now = datetime.now()

print('now  : ', now)

now = datetime(2015, 5, 18, 17, 2, 10, 871012)
dt = now.replace(tzinfo=tz_utc_8)  # 强制设置为UTC+8:0
print(dt)

# 时区转换
print(' 时区转换')
# utcnow()获取当前时区
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
print('utc_dt: ', utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('转换为北京时区: ', bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
print('转换为东京时区: ', tokyo_dt)

# astimezone()将bj_dt转换时区为东京时间:
tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
print("北京转东京: ", tokyo_dt2)
