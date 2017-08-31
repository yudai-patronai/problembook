A = 84589
C = 45989
M = 217728
__next = 0

def choice(l):
    return l[randrange(0, len(l))]


def randint(a, b):
    return randrange(a, b+1)


def __random(cur):
    return (A * cur + C) % M


def __randomint():
    return seed(__random(__next))


def randrange(a, b):
    return a + (b-a)*__randomint()//M


def sample(l, k):
    idx = list(range(len(l)))
    shuffle(idx)
    return [l[i] for i in sorted(idx[:k])]


def seed(seed):
    global __next
    __next = seed
    return __next


def shuffle(l):
    for i in range(len(l)-1, 0, -1):
        j = randint(0, i)
        l[i], l[j] = l[j], l[i]
