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
print(list(ts))

# itertools.cycle()
cs = itertools.cycle('abc')
t = 10
for c in cs:
  print(c, end='')
  t -= 1
  if t == 0:
    break
print()
# itertools.repeat()
ns = itertools.repeat('a', 3)
for n in ns:
  print(n, end='')
print()
# itertools提供的几个迭代器操作函数更加有用：
# chain()
for c in itertools.chain('abc', 'xyz'):
  print(c, end='')
print()

# groupby()
for key, group in itertools.groupby('AAABBBCCAAA'):
  print(key, list(group))

for key, group in itertools.groupby('AaaBBbCcAAaa', lambda c: c.upper()):
  print(key, list(group))


# permutations
friends = ['superman', 'batman', 'spiderman']
print(list(itertools.permutations(friends, r=2)))
# combinations
print(list(itertools.combinations(friends, r=2)))
