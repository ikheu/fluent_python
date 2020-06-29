import math
import reprlib
from array import array


class Vector:
    typecode = 'd'
    # 采用的直角坐标系，可以改进，参考sicp
    def __init__(self, components):
        self._components = array(self.typecode, components) 
    
    def __iter__(self):
        return iter(self._components)

    def __repr__(self):
        components = reprlib.repr(self._components)
        components = components[components.find('[') : -1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.sqrt(sum(x*x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(memv)
    

if __name__ == '__main__':
    v = Vector([3, 4])
    print(abs(v))
    if v:
        print('ok')
    print(v)
    print(format(v, '.3f'))
    hash(v)
    print(repr(v))
    print({v})
    # print(v.__dict__) # 使用了 __slots__ 就没有 __dict__这个东西了
    print(dir(v))
