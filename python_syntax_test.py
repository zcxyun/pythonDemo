import logging
from pprint import pprint
import random
from pydash import py_
import json
logging.basicConfig(level=logging.INFO)

a = [1, 2, 3, 2, 3, 4]
b = [4, 5, 6]
c = [7, 8, 9]
d = [1, [2], [[3]], 4]

data = [
    {'id': 9, 'name': 'zcx1', 'age': 1},
    {'id': 3, 'name': 'zcx3', 'age': 1},
    {'id': 1, 'name': 'zcx1', 'age': 1},
    {'id': 2, 'name': 'zcx2', 'age': 1},
    {'id': 3, 'name': 'zcx3', 'age': 1},
    {'id': 3, 'name': 'zcx3', 'age': 1},
    {'id': 4, 'name': 'zcx4', 'age': 1},
]

me = data[0]

# class User:
#     def __init__(self, name='zcx', age=18):
#         self.name = name
#         self.age = age
#     def __repr__(self):
#         return f'{self.name} - {self.age}'

# user1 = User()
# user2 = User('superman', '2999')
# user3 = User('spiderman', '39')
# user4 = User('batman', '45')

from datetime import datetime

date = datetime.strptime('2010-2-2 12:1:12', '%Y-%m-%d %H:%M:%S')
print(date.strftime('%Y-%m-%d'))
