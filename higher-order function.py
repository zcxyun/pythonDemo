# 测试reduce()
from functools import reduce
def add(x, y):
    return x + y

def fn(x, y):
    return x * 10 + y


##print(reduce(fn, range(0,10,2)))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

##print(str2int('12435345435') == int( '12435345435'))

# 测试filter()
def is_odd(n):
    return n % 2 == 1
##print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))

# 用filter() 求素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n
def _not_divisible(n):
    return lambda x: x % n > 0
def primes():
    yield 2
    it = _odd_iter()    # 初始序列
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)
for n in primes():
    if n < 100:
        print(n)
    else:
        break
