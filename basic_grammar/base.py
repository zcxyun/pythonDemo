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

# dir(), __dict__, vars() ==============================================
# class A:
#     one = 1
#     two = 2
#     def __init__(self):
#         self.three = 3

# class T(A):
#     sex = True
#     def __init__(self):
#         self.name = 'sdf'
#         self.age = 13

#     def isset(self):
#         pass

# t = T()
# print(dir(t))
# print()
# print(dir(T))
# print()
# print(vars(t))
# print(t.__dict__)
# print()
# print(vars(T))
# print(T.__dict__)
