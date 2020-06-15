import time
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        elspsed = time.perf_counter() - t0
        arg_list = []
        if args:
            arg_list.append(', '.join(repr(arg) for arg in args))
        if kwargs:
            arg_list.append(', '.join('%s=%r' % (k, w) for k, w in kwargs.items()))
        arg_str = ', '.join(arg_list) 
        print("[%0.8fs]%s(%s)->%r" % (elspsed, func.__name__, arg_str, res))
        return res
    return clocked

@clock
def test(a1, a2=None):
    time.sleep(1)
    print('ok')

# test(10, a2=3)