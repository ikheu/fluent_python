from inspect import getgeneratorstate

def simple_courtine():
    print('started')
    x = yield 'hi'
    print('received: %s' % x)

if __name__ == '__main__':
    coro = simple_courtine()
    print(getgeneratorstate(coro))
    print(coro.send(None))
    print(getgeneratorstate(coro))
    print(coro.send('there'))
