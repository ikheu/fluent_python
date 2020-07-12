from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)

# async def foo():
#     pass

# print(type(foo))
# print(type(foo()))

# the delegating generator
def grouper(results, key):
    while True: # yield from 接收到数据后会创建新的生成器 av。 这里的 while True 可以避免出现 StopIteration。也可以在 （1）处的 for 循环内部哪里捕获错误。
        av = averager()
        results[key] = yield from av


# the client code, a.k.a. the caller
def main(data):
    results = {}
    for key, values in data.items(): # （1）
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None) # important!
        # group.close() # 这里可以显式地关闭生成器，避免继续接收数据，继续接收数据会接着在 key 上处理
        # print(getgeneratorstate(group))
    print(results)


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m':
        [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg':
         [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m':
        [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


if __name__ == '__main__':
    main(data)
