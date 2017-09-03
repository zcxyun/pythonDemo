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

dog = Dog()
dog.run()
cat = Cat()
cat.run()
animal = Animal()
animal.run_twice(Tortoise())
animal.run_twice(Dog())
animal.run_twice(Cat())
