# 继承
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name

    def get_score(self):
        return self.__score
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

##bart = Student('zcx', 100)
##bart.set_score(11)
##print(bart.get_name(),bart.get_score())
##print(bart._Student__name)

# 鸭子类型
class Animal(object):
    def run(self):
        print('Animal is running...')
    def run_twice(self,animal):
        animal.run()
        animal.run()
class Dog(Animal):
    def run(self):
        print('Dog is running...')
class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

##dog = Dog()
##dog.run()
##cat = Cat()
##cat.run()
##animal = Animal()
##animal.run_twice(Tortoise())
##animal.run_twice(Dog())
##animal.run_twice(Cat())

# __slots__

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

# 使用@property
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

class Student(object):

    @property
    def score(self):
        return self._score
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be a integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0-100')
        self._score = value

s = Student()
s.score = 63
print(s.score)




