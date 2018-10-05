# __slots__ ==========================================================

##class Student(object):
##    pass
##s = Student()
##s.name = 'zcx'
##print(s.name)
##
##def set_age(self, age):
##    self.age = age
##from types import MethodType
##s.set_age = MethodType(set_age, s)
##s.set_age(25)
##print(s.age)

#给一个实例绑定的方法，对另一个实例是不起作用的
##s2 = Student()
##s2.set_age(22)

# 为了给所有实例都绑定方法，可以给class绑定方法
##def set_score(self, score):
##    self.score = score
##Student.set_score = set_score
##s.set_score(100)
##print(s.score)
##s2.set_score(99)
##print(s2.score)

# 使用__slots__
# 如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性
##class Student(object):
##    __slots__ = ('name', 'age')
##s = Student()
##s.name = 'zcx'
##s.age = 25
##s.score = 89
##class GraduateStudent(Student):
##    pass
##    __slots__ = ('score',)
##g = GraduateStudent()
##g.age = 88
##print(g.age)
# 设置一个类变量好像不受__slots__影响，实例变量依然能访问
##GraduateStudent.age2 = 3
##print(GraduateStudent.age2)
##print(g.age2)

# 使用@property ==========================================================
##class Student(object):
##    def get_score(self):
##        return self._score
##    def set_score(self, value):
##        if not isinstance(value, int):
##            raise ValueError('score must be a integer!')
##        if value < 0 or value > 100:
##            raise ValueError('score must between 0-100')
##        self._score = value
##s = Student()
##s.set_score(4)
##print(s.get_score())

##class Student(object):
##
##    @property
##    def score(self):
##        return self._score
##    @score.setter
##    def score(self, value):
##        if not isinstance(value, int):
##            raise ValueError('score must be a integer!')
##        if value < 0 or value > 100:
##            raise ValueError('score must between 0-100')
##        self._score = value

##s = Student()
##s.score = 63
##print(s.score)

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
