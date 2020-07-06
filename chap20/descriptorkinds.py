class Managed:
    def spam(self):
        pass

def foo():
    pass

if __name__ == '__main__':
    m = Managed()
    print(m.spam)
    print(Managed.spam)
    print(dir(m.spam))
    print(dir(Managed.spam))
    print(dir(foo))
