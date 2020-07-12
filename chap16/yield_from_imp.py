from inspect import getgeneratorstate
import types

# the subgenerator
def counter():
    total = 0.0
    count = 0
    while True:
        term = yield
        if term is None:
            break
        1 / term
        count += 1
    return count


def grouper(results, key):
    while True:
        results[key] = yield from counter()


def grouper1(results, key):
    while True:
        _i = iter(counter())
        try:
            _y = next(_i)
            is_gen = isinstance(_i, types.GeneratorType) # 判断是生成器还是一般的迭代器
            while 1:
                _s = yield _y # 产出 next 的返回值，即自生成器的第一个 yield 的值；等待调用方传递的
                if is_gen:
                    _y = _i.send(_s) # 
        except StopIteration as _e:
            _r = _e.value
        results[key] = _r


def main():
    results = {}
    key = 'k'
    values = [1, 2, 0, 4]
    group = grouper1(results, key)
    next(group)
    for value in values:
        group.send(value)
    group.send(None)
    print(results)

if __name__ == '__main__':
    main()
