#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# 实现上下文管理是通过__enter__和__exit__这两个方法实现的
# class Query(object):

#   def __init__(self, name):
#     self.name = name
#   def __enter__(self):
#     print('Begin')
#   def __exit__(self, exc_type, exc_value, traceback):
#     if exc_type:
#       print('Error')
#     else:
#       print('End')
#   def query(self):
#     print('Query info about %s' % self.name)

# with Query('zcx') as q:
#   q.query()

# @contextmanager test
from contextlib import contextmanager

class Query(object):

  def __init__(self, name):
    self.name = name
  def query(self):
    print('Query info about %s' % self.name)

@contextmanager
def create_query(name):
  print('Begin')
  q = Query(name)
  yield q
  print('End')

with create_query('zcx') as q:
  q.query()

# 很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现
@contextmanager
def tag(name):
  print('<%s>' % name)
  yield
  print('</%s>' % name)
with tag('h1'):
  print('hello')
  print('world')

# 如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对。例如，用with语句使用urlopen()：
from contextlib import closing
from urllib.request import urlopen

with closing(urlopen('http://www.python.org')) as page:
  for line in page:
    print(line)

# closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：

@contextmanager
def closing(thing):
  try:
    yield thing
  finally:
    thing.close()


