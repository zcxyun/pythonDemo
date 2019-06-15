# 装饰器在模块导入时调用=========================================

registry = []

def register(func):
    print('running register (%s)' % func)
    registry.append(func)
    return func

@register
def f1():
    print('running f1()')
@register
def f2():
    print('running f2()')

def f3():
    print('running f3()')

def main():
    print('running main()')
    print('registry ->', registry)
    f1()
    f2()
    f3()

if __name__ == '__main__':
    main()


# 装饰器 ================================================================
# import functools
# from inspect import isfunction

# def log(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('begin call')
#             print('text: %s' % (text if isinstance(text, str) else 'no log parameter'))
#             func(*args, **kw)
#             print('end call')
#         return wrapper
#     if isfunction(text):
#         return decorator(text)
#     else:
#         return decorator

# @log('sdfsf')
# def now():
#   print('now is time to go')

# @log
# def future():
#   print('future will come now')

# now()
# print('================================')
# future()
