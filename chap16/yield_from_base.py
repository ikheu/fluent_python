def gen():
    for c in 'AB':
        yield c
    for i in range(2):
        yield i


def gen1():
    yield from 'AB'
    yield from range(2)


# await 与 yield from 并不等价
async def foo1():
    return 'AB'

async def foo2():
    return range(2)

async def gen2():
    await foo1()
    await foo2()


import asyncio


print(list(gen()))
print(list(gen1()))

print(type(gen1()))
print(type(gen2()))

loop = asyncio.get_event_loop()
# print(loop.run_until_complete(list(gen2())))
