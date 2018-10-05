# test __getitem__   ===============================================
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
