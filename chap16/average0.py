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
    next(av)
    cur = av.send(10)
    print(cur)
    cur = av.send(20)
    print(cur)
