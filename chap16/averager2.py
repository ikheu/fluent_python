from functools import wraps
from collections import namedtuple


Result = namedtuple('Result', 'count average')


def couroutine(func):
    @wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen
    return primer


@couroutine
def averager():
    count = 0
    total = 0
    res = None
    while True:
        item = yield
        if item is None:
            break
        count += 1
        total += item
        res = total / count
    return Result(count, res)


if __name__ == '__main__':
    av = averager()
    av.send(10)
    av.send(20)
    try:
        av.send(None)
    except StopIteration as exec:
        print(exec.value)
