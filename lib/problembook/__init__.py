import traceback
import functools
import string
import math

BASE = len(string.ascii_uppercase)


class FakeArgs:

    def __init__(self, **kwargs):
        self.dict = kwargs

    def __getattr__(self, item):
        return getattr(super(), item) if hasattr(super(), item) else self.dict.get(item, None)

    def __getstate__(self):
        return self.dict.copy()

    def __setstate__(self, state):
        self.dict = state


def nth(i):

    def f(l):
        return l[i]

    return f


first = nth(0)
second = nth(1)


def problem_shortname(n, max):

    r = []
    for k in range(math.ceil(math.log(max, BASE))):
        r.append(n % BASE)
        n //= BASE

    return ''.join(reversed([string.ascii_uppercase[i] for i in r]))


def wrap_exception(f):
    '''Исключительно для отладочных целей'''

    @functools.wraps(f)
    def worker(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            traceback.print_exc()

    return worker