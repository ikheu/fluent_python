def deco(fun):
    def inner():
        print('running inner()')
    return inner


@deco
def target():
    print('running target()')


"""
@deco 等价于：
def target():
    print('running target()')
target = deco(target)
"""


target()


def deco1(fun):
    print('hi')


@deco1
def target1():
    print('running target()')


target1()  # 这里报错，因为装饰器没有返回函数，不可调用
