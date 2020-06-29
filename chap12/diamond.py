class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def __new__(cls):
        print('new b')
        return super().__new__(cls)
    
    def __init__(self):
        print(dir(self))
        print(self.__class__)
        print(self.attr1)
        print('init b')

    def pong(self):
        print('pong:', self)


class C(A):
    def __init__(self):
        print('init c')

    def pong():
        print('PONG:', self)


class D(B, C):
    def __new__(cls):
        print('new d')
        return super().__new__(cls)

    def __init__(self):
        self.ss = 10
        print('init d')
        self.attr1 = 10
        super().__init__()

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)

    def ss():
        return 1

if __name__ == '__main__':
    d = D()
    print(isinstance(d, B))
    print(isinstance(d, C))
    print(d.ss)

