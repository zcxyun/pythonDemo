#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple

# namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1,2)
print(p.x, p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))

# deque
from collections import deque

q = deque(['a', 'b', 'c'])
q.append('x')
q.pop()
q.appendleft('y')
q.popleft()
print(q)

# defaultdict
from collections import defaultdict

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

# OrderedDict
from collections import OrderedDict

d = dict([('a', 1), ('b', 2), ('c', 3)])
print(d)
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od.keys()))

# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super(LastUpdatedOrderedDict, self).__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
            last = self.popitem(last=False)
            print('remove:', last)
        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))
        OrderedDict.__setitem__(self, key, value)
luod = LastUpdatedOrderedDict(2)
luod['a'] = 1
luod['b'] = 2
luod['a'] = 3
luod['c'] = 2
print(luod)

# Counter
from collections import Counter
c = Counter()
for ch in 'programming':
  c[ch] = c[ch] + 1
print(c)
