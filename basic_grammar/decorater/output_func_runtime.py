# import time

# def clock(func):
#     def clocked(*args):
#         t0 = time.perf_counter()
#         result = func(*args)
#         elapsed = time.perf_counter() - t0
#         name = func.__name__
#         args_str = ', '.join(repr(arg) for arg in args)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args_str, result))
#         return result
#     return clocked

# 上述装饰器有几个缺点：
#   1. 不支持关键字参数
#   2. 而且遮盖了被装饰函数的 __name__, __doc__属性
# functools.wraps 装饰器把相关的属性从 func 复制到 clocked 中

# import functools

# def clock(func):
#     @functools.wraps(func)
#     def clocked(*args, **kw):
#         t0 = time.time()
#         result = func(*args, **kw)
#         elapsed = time.time() - t0
#         name = func.__name__
#         arg_lst = []
#         if args:
#             arg_lst.append(', '.join(repr(arg) for arg in args))
#         if kw:
#             pairs = ['%s=%r' % (k, w) for k, w in kw.items()]
#             arg_lst.append(', '.join(pairs))
#         args_str = ', '.join(arg_lst)
#         print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, args_str, result))
#         return result
#     return clocked

# @clock
# def snooze(seconds, **kw):
#     time.sleep(seconds)

# @clock
# def factorial(n):
#     return 1 if n < 2 else n * factorial(n-1)



# if __name__ == '__main__':
#     print('*' * 40, 'calling snooze')
#     snooze_name = snooze.__name__
#     print(snooze_name)
#     snooze(1, a=1)
#     print('*' * 40, 'calling factorial(6)')
#     print('6! = ', factorial(6))


# 参数化装饰器====================================================
import time

default_fmt = '[{elapsed:0.8f}s] {name}({args_str} -> {result})'
def clock(fmt = default_fmt):
    def decorator(func):
        def clocked(*args):
            t0 = time.time()
            result = func(*args)
            elapsed = time.time() - t0
            name = func.__name__
            args_str = ', '.join(repr(arg) for arg in args)
            print(fmt.format(**locals()))
            return result
        return clocked
    return decorator

if __name__ == '__main__':
    @clock()
    def snooze(seconds):
        time.sleep(seconds)
    for i in range(3):
        snooze(0.123)
