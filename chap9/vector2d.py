import math
from array import array


class Vector2d:
    typecode = 'd'

    def __init__(self, x ,y):
        self.x = float(x)
        self.y = float(y)
    
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
        class_name = typ(self).__name__
        return '{} ({!r}, {!r})' % (class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        pass


if __name__ == '__main__':
    v = Vector2d(3, 4)
    print(v + v)
    print(v * 3)
    print(abs(v))
    if v:
        print('ok')
    print(v)
