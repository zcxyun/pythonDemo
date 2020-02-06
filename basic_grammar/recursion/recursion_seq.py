import logging

logging.basicConfig(level=logging.INFO)

def sum_loop(n):
    sum_number = 0
    for i in range(1, n+1):
        sum_number += i
    return sum_number

logging.info('求和 用循环: {}'.format(sum_loop(100)))

def sum_recursion(n):
    if n == 1:
        return 1
    else:
        return sum_recursion(n-1) + n

logging.info('求和 用递归: {}'.format(sum_recursion(100)))


def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

logging.info('斐波那契序列: {}'.format(fibonacci(4)))


def factorial(n):
    if n == 0:
        return 1
    else:
        return factorial(n-1) * n

logging.info('阶乘: {}'.format(factorial(5)))

