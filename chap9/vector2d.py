import math
from array import array


class Vector2d:
    typecode = 'd'
    __slots__ = ('__x', '__y')
    # 采用的直角坐标系，可以改进，参考sicp
    def __init__(self, x ,y):
        self.__x = float(x)
        self.__y = float(y)
    
    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __add__(self, other):
        return Vector2d(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector2d(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __bool__(self):
        return bool(self.x) and bool(self.y)
    
    # repr 用于终端调试，不定义的话输出不友好；__str__ 用于转化为字符串
    def __repr__(self):
        class_name = type(self).__name__
        print(*self)
        return '{} ({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes([ord(self.typecode)]) + bytes(array(self.typecode, self))

    def __format__(self, fmt=''):
        items = (format(c, fmt) for c in self)
        return '({}, {})'.format(*items)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:].cast(typecode))
        return cls(*memv)
    

if __name__ == '__main__':
    v = Vector2d(3, 4)
    print(v + v)
    print(v * 3)
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
