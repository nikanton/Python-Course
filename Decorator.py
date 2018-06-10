import sys
import functools
import time


def profiler(func):
    @functools.wraps(func)
    def decorated(*args, **kwargs):
        if decorated.first_call:
            decorated.first_call = False
            decorated.calls = 1
            decorated.last_time_taken = time.time()
            res = func(*args, **kwargs)
            decorated.last_time_taken = time.time() - decorated.last_time_taken
            decorated.first_call = True
            return res
        else:
            decorated.calls += 1
            return func(*args, **kwargs)
    decorated.first_call = True
    decorated.calls = 0
    decorated.last_time_taken = 0.
    return decorated

exec(sys.stdin.read())

@profiler
def f(a):
    if a > 0:
        return f(a - 1)
    else:
        return 0
print f(6)
print f.calls