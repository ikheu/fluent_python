from clock import clock
import functools


@functools.lru_cache()
@clock
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-2) + fib(n-1) 


fib(6)
