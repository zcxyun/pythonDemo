from pydash import py_

data = [
    {'id': 1, 'name': 'zcx1'},
    {'id': 1, 'name': 'zcx1'},
    {'id': 2, 'name': 'zcx2'},
    {'id': 3, 'name': 'zcx3'},
    {'id': 3, 'name': 'zcx3'},
    {'id': 3, 'name': 'zcx3'},
    {'id': 4, 'name': 'zcx4'},
]

print(py_.group_by(data, 'id'))
class Cat:
    def __init__(self, name='zcx', gender='male', age=18):
        self.name = name
        self.gender = gender
        self.age = age
    def __repr__(self):
        return '{}-{}-{}'.format(self.name, self.gender, self.age)

cat1 = Cat()
cat2 = Cat('jack', 'male', 20)
cat3 = Cat('jack', 'male', 24)
cat4 = Cat('jack', 'male', 24)
cat5 = Cat('jack', 'male', 21)
cat6 = Cat('jack', 'male', 22)
cat7 = Cat('jack', 'male', 22)
cat8 = Cat('jack', 'male', 22)
cats = [cat1, cat2, cat3, cat4, cat5, cat6, cat7, cat8]
n = py_.group_by(cats, 'age')
print(n)
