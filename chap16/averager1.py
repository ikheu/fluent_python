from functools import wraps


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
        item = yield res
        count += 1
        total += item
        res = total / count

if __name__ == '__main__':
    av = averager()
    cur = av.send(10)
    print(cur)
    cur = av.send(20)
    print(cur)
