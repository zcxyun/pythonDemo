# #! /usr/bin/env python3
# # -*- coding: utf-8 -*-
from pprint import pprint
from datetime import datetime, timedelta, date

# # 获取当前日期和时间
# now = datetime.now()
# print(now)
# # 获取指定日期和时间
# dt = datetime(2017, 4, 19, 12, 39)
# print(dt)
# # datetime 转换为 timestamp
# print(dt.timestamp())
# # timestamp 转换为 datetime
# # 注意到timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的。上述转换是在timestamp和本地时间做转换。
# # 本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
# print(datetime.fromtimestamp(dt.timestamp()))
# # timestamp也可以直接被转换到UTC标准时区的时间
# print(datetime.utcfromtimestamp(dt.timestamp()))

# # str 转换为 datetime
# cday = datetime.strptime('2017-9-29 19:39:34', '%Y-%m-%d %H:%M:%S')
# print(cday)
# print(datetime.strptime('20183sdf', '%Y-%m-%d %H:%M:%S'))
# # datetime 转换为 str
# print(now.strftime('%a, %b %d %H:%M'))

# # datetime 加减
# print(now + timedelta(hours=10))
# print(now + timedelta(days=1))
# print(now + timedelta(days=2, hours=12))

# ----------------------
# now = datetime.now()
# print(now.year)
# print(now.month)
# print(now.day)
# print(now.hour)
# print(now.minute)
# print(now.second)
# print(now.date())
# print(now.time())

# 时间比大小
# now = datetime.now()
# ago_30_days = now - timedelta(days=30)
# print((now - ago_30_days).days)

datetime.strptime('sdfs', '%Y-%m-%d %H:%M:%S')
