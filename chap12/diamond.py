class A:
    def ping(self):
        print('ping:', self)


class B(A):
    def __new__(cls):
        print('new b')
        return super().__new__(cls)
    
    def __init__(self):
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
        self.__dict__.update({'ss': 10})
        print('init d')
        self.attr1 = 10
        super().__init__()

    @property
    def ss(self):
        return 1

    def ping(self):
        super().ping()
        print('post-ping:', self)

    def pingpong(self):
        self.ping()
        super().ping()
        self.pong()
        super().pong()
        C.pong(self)


if __name__ == '__main__':
    d = D()
    print(isinstance(d, B))
    print(isinstance(d, C))
    print(d.ss)
    print(dir(d))
    print(d.__dict__)
    D.ss = 'foo'
    print(d.ss)
