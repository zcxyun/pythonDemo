import reprlib
from array import array
import math

class Vector:
    typecode = 'd'
    def __init__(self, components):
        self._components = array(self.typecode, components)

    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self._components))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + (bytes(self._components)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self._components))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv)

v1 = Vector([1,2,3])
print(v1)
print('%r' % v1)
a,b,_ = v1
print(a,b)
print(bytes(v1))
print(Vector.frombytes(bytes(v1)))
print(abs(v1))
print(bool(v1))
