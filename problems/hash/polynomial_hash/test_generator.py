from lib.testgen import TestSet
from lib.random import seed, randint


seed(42)

RANDOM_TESTS = 3

MIN_MODULE = 10
MAX_MODULE = 10**6

MIN_BASE = 2
MAX_BASE = 1000

MIN_STR_LEN = 5
MAX_STR_LEN = 100

ORD_FIRST = ord('a')
ORD_LAST = ord('z')

def gen_test():
    # returns base, module, string
    
    base = randint(MIN_BASE, MAX_BASE)
    module = randint(MIN_MODULE, MAX_MODULE)
    
    # gen string
    s = ''
    s_len = randint(MIN_STR_LEN, MAX_STR_LEN)

    for i in range(s_len):
        char_ord = randint(ORD_FIRST, ORD_LAST)
        s += chr(char_ord)

    return base, module, s

def question(base, module, s):
    return '{} {}\n{}\n'.format(base, module, s)

def answer(h):
    return '{}\n'.format(h)

# да, это грязно
def poly_hash(p, m, s):
    # полиномиальный хеш справа-налево
    # строка s = s_0 s_1 .. s_i .. s_{n-1}
    # хеш =
    #  (o_0 * p^{len(s)-1} + o_1 * p^{len(s)-2} + ... + o_i * p^(len(s)-i-1) + ... + o_{n-2} * p + o_{n-1}) mod m
    #  где o_i = ord(s_i)

    h = 0
    for c in s:
        h = ( (h * p) % m + ord(c)) % m  # % m внутренний для избежания переполнения (длинной арифметики)

    return h


tests = TestSet()

# ручные тесты
manual_tests = [ (2, 100, 'b', ), (3, 1000, 'abc')]
for t in manual_tests:
    tests.add(question(*t), answer(poly_hash(*t)))

# случайные тесты
for i in range(RANDOM_TESTS):
    t_data = gen_test()
    tests.add(question(*t_data), answer(poly_hash(*t_data)))
