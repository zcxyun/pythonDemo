# test __getattr__ ==========================================================
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



# 在《编写高质量代码–改善python建议》中，看到了__getattr__()和__getattribute__()方法的区别，在此一记。
# __getattr__()和__getattribute__() 都是用于实例属性的获取和拦截（仅对实例属性有效，非类属性，类属性通过__set__ 和 __get__），__getattr__() 适用于未定义的属性，而，__getattribute__() 对于所有属性访问都会调用改方法，并且仅用于新式类。
# 两个区别主要如下：
# 1. __getattrobute__() 只要涉及到实例属性的访问就会调用该方法，如果属性不存在会抛出AttributeError 异常。
# 2. __getattr__() 在以下情况下调用：
# 2.1. 属性不在实例的__dict__中；
# 2.2. 属性不在其基类以及祖先类的__dict__ 中；
# 2.3. 出发AttributeError 异常时(不仅仅是__get_attribute__() 引发的异常，property中定义的get() 方法抛出的异常也会调用该方法。)
# 3. 当__getattr__ 和__getattribute__ 同时被定义时，要么显示在__getattribute__ 中调用，要么抛出AttributeError 异常，否则__getattr__ 永远不会被调用。
# __getattr__ 和__getattribute__ 都是Object 类中定义的默认方法，当覆盖这些方法时需要注意几点：
# 1. 避免无穷递归调用；
# 2. 访问未定义的属性。如果__getattr__() 方法中不抛出AttributeError 异常或者显示返回一个值，则会返回None，此时可能影响到程序的实际运行预期。
# 如果t不属于实例属性，打印警告信息，否则给c赋值。按照用户的理解本来应该是输出警告信息的，可实际却输出None。因为__getattr__ 没用抛出任何异常也没有返回一个值，None被作为默认值返回并且动态添加了t属性。
# 另外需要注意以下两点
# 1） 覆盖__getattribute__方法后，任何属性的访问都会调用用户定义的__getattribute__ 方法，性能上回有损耗，比使用默认的方法要慢；
# 2) 覆盖的__getattr__ 方法如果能够动态处理事先未定义的属性，可以更好实现数据隐藏。
# __getattribute__() 总会被调用，而__getattr__() 只有在__getattribute__() 中引发异常的情况下才会被调用。

class A(object):
    def __init__(self, name):
        self.name = name
        self.x = 20
    def __getattr__(self, name):
        print('calling __getattr__', name)
        if name == 'z':
            return self.x ** 2
        elif name == 'y':
            return self.x ** 3
    def __getattribute__(self, attr):
        try:
            return super(A, self).__getattribute__(attr)
        except KeyError:
            return 'default'

a = A('attribute')
print(a.name)
print(a.z)
# print(hasattr(a, 't'))
if hasattr(a, 't'):
    c = a.t
    print(c)
else:
    print('instanc a has no attribute t')

