#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import pickle

d = dict(name = 'zcx', age = 29, score = 88)
data = pickle.dumps(d)
print(data)

reborn = pickle.loads(data)
print(reborn)

with open('dumps.txt', 'wb') as f:
  pickle.dump(d, f)

with open('dumps.txt', 'rb') as f:
  d = pickle.load(f)
print(d)
