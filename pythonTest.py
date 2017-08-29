##import os
##L = [('Bob', 88), ('Adam', 88), ('Bart', 88), ('Lisa', 88),]
##filelist = [f for f in os.listdir('.')]
##print(filelist)
from functools import reduce
def add(x,y):
    return x + y
print(list(range(10))[::2])
print(reduce(add, range(10)[::2]))

