# test __str__ __repr__====================================
# class Student(object):
#     def __init__(self, name):
#         self.name = name
#     def get_name(self):
#         return self.name
#     def __str__(self):
#         return 'Student object  (name: %s)' % (self.name)
#     def __repr__(self):
#         return self.__str__()
#     __repr__ = __str__
# s = Student('xvc')
# # 类可以直接访问实例方法，不过好像得传入实例 =============================
# name = Student.get_name(Student('d'))
# print(name)
# print(s)
