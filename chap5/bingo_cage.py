import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick form empty BingoCage') # 这里抛出的错误更有意义， IndexError 更细节
    
    def __call__(self):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(1, 10))
    for i in range(9):
        res = bingo()
        print(res)
    print(callable(bingo))
    print(dir(bingo))
    print(bingo.__dict__)
    print(BingoCage.__dict__)
