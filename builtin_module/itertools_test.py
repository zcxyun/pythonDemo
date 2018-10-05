#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

# itertools提供的几个“无限”迭代器
# itertools.count(1)
natuals = itertools.count(1)
# for n in natuals:
#   print(n)
#   if n >= 100:
#     break
# itertools.takewhile()
ts = itertools.takewhile(lambda x: x<=10, natuals)
print(ts)

# itertools.cycle()
cs = itertools.cycle('abc')
t = 10
for c in cs:
  print(c)
  t -= 1
  if t == 0:
    break

# itertools.repeat()
ns = itertools.repeat('a', 3)
for n in ns:
  print(n)

# itertools提供的几个迭代器操作函数更加有用：
# chain()
for c in itertools.chain('abc', 'xyz'):
  print(c)

# groupby()
for key, group in itertools.groupby('AAABBBCCAAA'):
  print(key, list(group))

for key, group in itertools.groupby('AaaBBbCcAAaa', lambda c: c.upper()):
  print(key, list(group))



