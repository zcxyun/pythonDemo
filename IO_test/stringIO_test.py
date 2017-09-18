#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from io import StringIO

# write to StringIO:
# f = StringIO()
# f.write('hello')
# f.write(' ')
# f.write('world!')

# print(f.getvalue())

# read from StringIO:
# f = StringIO('床前明月光, \n疑是地上光, \n举头望明月, \n低头思故乡')
f = StringIO('abc, \ndef, \nghi, \njkl')
while True:
  s = f.readline()
  if s == '':
    break
  print(s.strip())
