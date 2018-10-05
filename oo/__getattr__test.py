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
