# 继承 ########################################################
##class Student(object):
##    def __init__(self, name, score):
##        self.__name = name
##        self.__score = score
##
##    def get_name(self):
##        return self.__name
##    def set_name(self, name):
##        self.__name = name
##
##    def get_score(self):
##        return self.__score
##    def set_score(self, score):
##        if 0 <= score <= 100:
##            self.__score = score
##        else:
##            raise ValueError('bad score')
##
##    def print_score(self):
##        print('%s: %s' % (self.__name, self.__score))

##bart = Student('zcx', 100)
##bart.set_score(11)
##print(bart.get_name(),bart.get_score())
##print(bart._Student__name)

# 鸭子类型 ########################################################
##class Animal(object):
##    def run(self):
##        print('Animal is running...')
##    def run_twice(self,animal):
##        animal.run()
##        animal.run()
##class Dog(Animal):
##    def run(self):
##        print('Dog is running...')
##class Cat(Animal):
##    def run(self):
##        print('Cat is running...')
##
##class Tortoise(Animal):
##    def run(self):
##        print('Tortoise is runniwly...')

##dog = Dog()
##dog.run()
##cat = Cat()
##cat.run()
##animal = Animal()
##animal.run_twice(Tortoise())
##animal.run_twice(Dog())
##animal.run_twice(Cat())

# __slots__ ########################################################

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

# 使用@property ########################################################
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

# Python的方法主要有3个,即静态方法(staticmethod),类方法(classmethod)和实例方法 ###############
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


# 定制类 ########################################################
# test __str__ __repr__
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
# # 类可以直接访问实例方法，不过好像得传入实例 #####################
# name = Student.get_name(Student('d'))
# print(name)
# print(s)

# test __iter__ __next__
# class Fib(object):
#   def __init__(self):
#     self.a, self.b = 0, 1
#   def __iter__(self):
#     return self
#   def __next__(self):
#     self.a, self.b = self.b, self.a + self.b
#     if self.a > 10000:
#       raise StopIteration()
#     return self.a
# for n in Fib():
#   print(n)

# test __getitem__
# class Fib(object):
#   def __getitem__(self, n):
#     a, b = 1, 1
#     for x in range(n):
#       a, b = b, a + b
#     return a
# f = Fib()
# for x in range(11):
#   print(f[x])

#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
# class Fib(object):
#   def __getitem__(self, n):
#     if isinstance(n, int):
#       a, b = 1, 1
#       for x in range(n):
#         a, b = b, a + b
#       return a
#     if isinstance(n, slice):
#       start = n.start
#       stop = n.stop
#       if start is None:
#         start = 0
#       a, b = 1, 1
#       L = []
#       for x in range(start, stop):
#         L.append(a)
#       a, b = b, a + b
#       return L
# f = Fib()
# print(f[:10])

# test __getattr__ #########################
# 只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
# 此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError的错误：
# class Student(object):
#   def __init__(self):
#     self.name = 'zcx'
#   def __getattr__(self, attr):
#     if attr == 'score':
#       return 11
#     elif attr == 'age':
#       return lambda: 23
#     raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
# s = Student()
# print(s.name)
# print(s.score)
# print(s.age())
# print(s.abs)

# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
# 这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
# 举个例子：
# 现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
# http://api.server/user/friends
# http://api.server/user/timeline/list
# 如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
# 利用完全动态的__getattr__，我们可以写出一个链式调用：
# class Chain(object):
#   def __init__(self, path=''):
#     self._path = path
#   def __getattr__(self, path):
#     return Chain('%s/%s' % (self._path, path))
#   def __str__(self):
#     return self._path
#   __repr__ = __str__
# print(Chain().status.user.timeline.list)

# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！还有些REST API会把参数放到URL中，比如GitHub的API：调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
# class Chain(object):
#   def __init__(self, path = 'GET '):
#     self._path = path
#   def __str__(self):
#     return self._path
#   __repr__ = __str__
#   def __getattr__(self, path):
#       return Chain("%s/%s" % (self._path, path))
#   def users(self, name):
#     return Chain("%s/users/:%s" % (self._path, name))
# print(Chain().users('zcxsfsdfsd').repos)

# test __call__
# 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
# class Student(object):
#     def __init__(self, name):
#       self._name = name
#     # def __call__(self):
    #   print('my name is %s' % self._name)
# s = Student('zcx')
# print(s())
# print(callable(s))
# print(callable(lambda x: x))
# print(callable(max))
# print(callable([1,2,3]))
# print(callable(None))
# print(callable('str'))

# 使用枚举类
from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
for name, member in Month.__members__.items():
  print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
  Sun = 0
  Mon = 1
  Tue = 2
  Wed = 3
  Thu = 4
  Fri = 5
  Sat = 6
for name, member in Weekday.__members__.items():
  print(name, '=>', member, ',', member.value)
