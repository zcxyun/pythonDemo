# 函数参数 ================================================================
# def add(x, y, z=2, *, a=5, **kw):
#   print(x, y, z, a, kw)
# add(1,2)
# add(1, z=4, y=2)

# 可变对象不能作为函数默认参数值，默认参数值会被放入函数对象的__defaults__属性中，若是可变对象改变自身，函数再次调用时默认参数值也会改变 ===========================================================================
# class A:
#     def __init__(self, passengers = []):
#             self.passengers = passengers

# b1 = [1,2,3]
# b2 = [4,5,6]
# a1 = A()
# a2 = A()
# a1.passengers.append(4)
# print(A.__init__.__defaults__)
# print(A.__init__.__defaults__[0] is a2.passengers)
# print(a1.passengers)
# print(a2.passengers)
