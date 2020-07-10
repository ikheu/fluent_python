from collections import namedtuple
Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        print('----')
        term = yield
        if term is None:
            break
        print(term)
        total += term
        count += 1
        average = total/count
    return Result(count, average)


# the delegating generator
def grouper(results, key):
    print('sssssssssssss')
    while True:
        print('ssssss')
        results[key] = yield from averager()
        print('----')



# the client code, a.k.a. the caller
def main(data):
    results = {}
    for key, values in data.items():
        print(type(grouper))
        group = grouper(results, key)
        print(type(group))
        # next(group)
    #     for value in values:
    #         group.send(value)
    #     group.send(None) # important!
    # print(results)


data = {
    'girls;kg':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    # 'girls;m':
    #     [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
#     'boys;kg':
#          [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
#     'boys;m':
#         [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}


def foo():
    print('---')
    yield 1

def foo1():
    print('---1')
    return 1

print(dir(foo))
print(dir(foo1))

print(foo())
print(foo1())

if __name__ == '__main__':
    main(data)
