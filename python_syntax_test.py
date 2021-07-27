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
s = 'abcdefghijklmnopqrstuvwxyz'

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


for i in data[0]:
    print(i)

class User:
    def __init__(self, name='zcx', age=18):
        self.name = name
        self.age = age
    @property
    def sex(self):
        return 1

    def keys(self):
        return ('name', 'age', 'sex')
    def __getitem__(self, key):
        return getattr(self, key)
    def __repr__(self):
        return f'{self.name} - {self.age}'

class Jack(User):
    def __init__(self, name='jack', age=20, sex=1):
        super().__init__(name, age)
        self.sex = sex

    def __repr__(self):
        return f'{self.name} - {self.age} - {self.sex}'

# jack = Jack()
# print(jack)

# res = User()
# print(dict(User()))
# print(vars(User()))

