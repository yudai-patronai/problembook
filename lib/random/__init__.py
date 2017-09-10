import math
import hashlib

A = 84589
C = 45989
M = 217728
__next = 0


def choice(l):
    return l[randrange(0, len(l))]


def randint(a, b=0):
    return randrange(a, b+1)


def __random(cur):
    return (A * cur + C) % M


def __randomint():
    return seed(__random(__next))


def random():
    return __randomint()/M


def randrange(a, b=0):
    if b == 0:
        b = a
        a = 0
    elif isinstance(a, float):
        a = math.ceil(a)
    return a + (b-a)*__randomint()//M


def __sample_small(l, k):
    idx = set()

    while len(idx) < k:
        idx.add(randrange(k))

    return [l[i] for i in idx]


def sample(l, k):
    if k < 10:
        return __sample_small(l, k)

    r = list(l[:k])

    for i in range(k, len(l)):
        j = randint(0, i)
        if j < k:
            r[j] = l[i]

    return r


def seed(seed):
    global __next
    __next = seed if isinstance(seed, int) else sum(hashlib.sha512(str(seed).encode()).digest())
    return __next


def shuffle(l):
    for i in range(len(l)-1, 0, -1):
        j = randint(0, i)
        l[i], l[j] = l[j], l[i]
