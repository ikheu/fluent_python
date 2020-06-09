import math

class Vector:
    def __init__(self, x ,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __abs__(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def __bool__(self):
        return bool(self.x) and bool(self.y)

    def __repr__(self):
        return 'Vector(%s, %s)' % (self.x ,self.y)


# repr 用于终端调试，不定义的话输出不友好；__str__ 用于转化为字符串

if __name__ == '__main__':
    v = Vector(3, 4)
    print(v + v)
    print(v * 3)
    print(abs(v))
    if v:
        print('ok')
    print(v)
