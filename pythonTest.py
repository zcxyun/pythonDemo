#import os
#L = [('Bob', 88), ('Adam', 88), ('Bart', 88), ('Lisa', 88),]
#filelist = [f for f in os.listdir('.')]
#print(filelist)
# from functools import reduce
# def add(x,y):
#     return x + y
# print(list(range(10))[::2])
# print(reduce(add, range(10)[::2]))

# 获取 全局变量 global
# a = 1
# def func():
#   global a
#   a = 2
#   print(a)
# func()
# print(a)

# 变量作用域是函数作用域, 函数未执行之前，作用域已经形成了，作用域链也生成了
# name = "lzl"
# def f1():
#     print(name)
# def f2():
#     name = "eric"
#     f1()
# f2()


li = [lambda : x for x in range(10)]
res = li[0]()
print(res)

