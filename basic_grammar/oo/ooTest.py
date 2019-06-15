# Python类的方法主要有3个,即静态方法(staticmethod),类方法(classmethod)和实例方法 ==========================================================
# def foo(x):
#    print("executing foo(%s)" % (x))

# class A(object):
#     def foo(self,x):
#         print("executing foo(%s,%s)" % (self,x))

#     @classmethod
#     def class_foo(cls,x):
#         print("executing class_foo(%s,%s)" % (cls,x))

#     @staticmethod
#     def static_foo(x):
#         print("executing static_foo(%s)" % x)

# a=A()
# print(a.foo('zcx1'))
# print(a.class_foo('zcx2'))
# print(a.static_foo('zcx3'))
# # 类无法调用实例方法，要想调用需要传入所有参数，也就是要传入第一个参数（实例）
# print(A.foo(A(), 'zcx4'))
# print(A.class_foo('zcx5'))
# print(A.static_foo('zcx6'))


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
