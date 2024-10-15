from functools import cache

__all__ = ['my_sum']


def my_sum(iterable):
    tot = 0
    for i in iterable:
        tot += i
    return tot


@cache
def factorial(n):
    return 1 if n <= 1 else n*factorial(n-1)
