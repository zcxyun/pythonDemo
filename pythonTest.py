# 列表生成式 ===============================================================
#import os
#L = [('Bob', 88), ('Adam', 88), ('Bart', 88), ('Lisa', 88),]
#filelist = [f for f in os.listdir('.')]
# print(filelist)

# reduce =================================================================
# from functools import reduce
# def add(x,y):
#     return x + y
# print(list(range(10))[::2])
# print(reduce(add, range(10)[::2]))

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

# lambda  ================================================================
# li = [lambda : x for x in range(10)]
# res = li[0]()
# print(res)

# set ====================================================================
# l = [1,2,3,5,6,7,8]
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d2 = dict({'Michael': 95, 'Bob': 75, 'Tracy': 85})
# # print(d,d2)
# s = set(l)
# # print(s.pop(), s.remove())
# print(l.pop(1), l.remove(8))
# print(l)

# 函数参数 ================================================================
# def add(x, y, z=2, *, a=5, **kw):
#   print(x, y, z, a, kw)
# add(1,2)
# add(1, z=4, y=2)

# 类属性和实例属性 ===========================================================
# class Student:
#   sum = 0
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age
#     Student.sum += self.age

#   @classmethod
#   def summer(cls):
#     print(Student.sum)

#   @staticmethod
#   def summer2():
#     print(Student.sum)

#   def summer3(self):
#     print(Student.sum)

# class Mary(Student):
#   pass

# stu = Student('jack', 18)
# stu2 = Student('mary', 20)
# mary = Mary('mary', 17)
# mary.summer()
# Mary.summer()
# mary.summer2()
# Mary.summer2()
# Student.__init__(stu, 'sdf', 18)
# print(stu.summer())

# 正则表达式 ===========================================================
# import re
# a = """
# 0c,
# 0c++,
# 0c#,
# 0python,
# 0css,
# 0html,
# 0java,
# 0javascript"""
# r = re.findall(r'[a-z+#]+', a)
# print(r)

# s = 'abc37d2d85'
# def convert(value):
#   matched = value.group()
#   return '90' if int(matched) >= 50 else '00'
# r = re.match(r'\d{2}', s)
# r1 = re.search(r'\d{3}', s)
# print(r, r1)

# s = 'life is short, so i use python'
# r = re.findall(r'(sh).*(so)', s)
# print(r)
# r1 = re.findall(r'li\w\w', s)
# print(r1)


# 枚举 ===============================================================
# from enum import Enum
# from enum import IntEnum,unique
# @unique
# class Vip(IntEnum):
#   RED = 1
#   YELLOW = 1
#   BLUE = 3
# print(Vip.YELLOW)

# from enum import Enum

# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)

# 闭包 =================================================================
# def a():
#   av = [1,2,3,4]
#   def b():
#     bv = 2
#     def c():
#       return av + bv
#     return c
#   return b
# c = a()()
# print(c.__closure__[1].cell_contents)

# print({'1','1'})
# print('1' == '1')
# print('1' is '1')
# print((1) == (1))
# print((1) is (1))
# print([1] is [1])

# 装饰器 ================================================================
# import functools
# from inspect import isfunction

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('begin call')
#             print('text: %s' % (text if isinstance(text, str) else 'no log parameter'))
#             func(*args, **kw)
#             print('end call')
#         return wrapper
#     if isfunction(text):
#         return decorator(text)
#     else:
#         return decorator

# @log('sdfsf')
# def now():
#   print('now is time to go')

# @log
# def future():
#   print('future will come now')

# now()
# print('================================')
# future()

# __slots__ @property =====================================================
# class Person(object):
#     """docstring for Person"""
#     __slots__ = ('__name', '__age')
#     def __init__(self, name = 'jack', age = 18):
#         super(Person, self).__init__()
#         self.__name = name
#         self.__age = age

#     @property
#     def name(self):
#         return self.__name
#     @name.setter
#     def name(self, name):
#         self.__name = name

#     @property
#     def age(self):
#         return self.__age
#     @age.setter
#     def age(self, age):
#         if not isinstance(age, int):
#             raise ValueError('年龄必须是整数！')
#         if age < 0 or age > 100:
#             raise ValueError('年龄超出范围！')
#         self.__age = age

#     def show(self):
#         print('My name is %s, and my age is %d' % (self.__name, self.__age))
#     def __call__(self):
#         pass
# jack = Person()
# jack.show()
# mary = Person('mary', 19)
# mary.show()
# mary.name = 'maryAn'
# mary.age = 21
# mary.show()

# print(callable(jack) == hasattr(jack, '__call__'))
# # print(type(jack.__call__))
# if hasattr(jack, '__getattr__'):
#     print('success')
# else:
#     print('fail')

a = map(lambda x: x*x, [1,2,3])
b = list(a)
print(b)
print(tuple(b))
# print(dict(b))
