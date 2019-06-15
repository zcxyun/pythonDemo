# 如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
# try:
#   print('try....')
#   r = 10 / int('0')
#   print('result:', r)

# except ValueError as e:
#   print('ValueError:', e)
# except ZeroDivisionError as e:
#   print('ZeroDivisionError:', e)
# else:
#   print('no error!')
# finally:
#   print('finally...')
#   print('END')

# test logging 记录错误 ###########################################
# import logging
# def foo(s):
#   return 10 / int(s)
# def bar(s):
#   return foo(s) * 2
# def main():
#   try:
#     bar('0')
#   except Exception as e:
#     logging.exception(e)
# main()
# print('END')

# test 抛出错误 #######################################################
#只有在必要的时候才定义我们自己的错误类型。如果可以选择Python已有的内置的错误类型（比如ValueError，TypeError），尽量使用Python内置的错误类型。
# class FooError(ValueError):
#   pass
# def foo(s):
#   n = int(s)
#   if n == 0:
#     raise FooError('invalid value: %s' % s)
#   return 10 / n
# foo('0')

# 另一种错误处理的方式 ############################################333
# 在bar()函数中，我们明明已经捕获了错误，但是，打印一个ValueError!后，又把错误通过raise语句抛出去了，这不有病么？
# 其实这种错误处理方式不但没病，而且相当常见。捕获错误目的只是记录一下，便于后续追踪。但是，由于当前函数不知道应该怎么处理该错误，所以，最恰当的方式是继续往上抛，让顶层调用者去处理。好比一个员工处理不了一个问题时，就把问题抛给他的老板，如果他的老板也处理不了，就一直往上抛，最终会抛给CEO去处理。
# def foo(s):
#   n = int(s)
#   if n == 0:
#     raise ValueError('invalid value: %s' % s)
#   return 10 / n
# def bar():
#   try:
#     foo('0')
#   except ValueError as e:
#     print('ValueError!')
#     raise
# bar()

# raise语句如果不带参数，就会把当前错误原样抛出。此外，在except中raise一个Error，还可以把一种类型的错误转化成另一种类型：
try:
  10 / 0
except ZeroDivisionError:
  raise ValueError('input error')
