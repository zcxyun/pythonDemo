from a2 import a2

print('a1 start')
def a1():
    print('this is %s' % 'a1')
    a2()

print('a1 end')

if __name__ == '__main__':
    a1()
