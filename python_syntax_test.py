# 列表生成式 ===============================================================
#import os
#L = [('Bob', 88), ('Adam', 88), ('Bart', 88), ('Lisa', 88),]
#filelist = [f for f in os.listdir('.')]
# print(filelist)


# 获取 全局变量 global ======================================================
# a = 1
# def func():
#   # global a
#   a = 22.2
#   print(a)
# func()
# print(a)

# 变量作用域是函数作用域, 函数未执行之前，作用域已经形成了，作用域链也生成了 =============
# _name = "lzl"
# def f1():
#     print(_name)
# def f2():
#     _name = "eric"
#     f1()
# f2()






from collections import defaultdict, namedtuple, OrderedDict, Iterable
from itertools import chain
from functools import reduce
from operator import add,mul
import json
from contextlib import contextmanager
import types

a = [1,1,2,2,3,3,3,3,4,5,5,9,7,21]
print(min(set(a), key=a.count))
print(isinstance({1:1}, Iterable))




