
import functools


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


def inc(x):
    return x + 1

def double(x):
    return 2*x
