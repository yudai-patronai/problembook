from lib.testgen import TestSet
from lib.random import randint

def dot_product(v1, v2):
    return sum(el1 * el2 for el1, el2 in zip(v1, v2))

def vec2str(vec):
    return ' '.join(map(str, vec))

def get_case(dim, v1, v2):
    result = dot_product(v1, v2)

    q_str = '{}\n{}\n{}'.format(dim, vec2str(v1), vec2str(v2))
    ans_str = str(result)
    return q_str, ans_str

def generate_random_case(dim, max_abs_val):
    v1 = [randint(-max_abs_val, max_abs_val) for _ in range(dim)]
    v2 = [randint(-max_abs_val, max_abs_val) for _ in range(dim)]
    return get_case(len(dim), v1, v2)


tests = TestSet()

tests.add(*get_case(1, [2], [3]))
tests.add(*get_case(3, [1, 2, 3], [1, 2, 3]))
tests.add(*get_case(3, [-1, 2, 3], [4, 5, 6]))

tests.add(*generate_random_case(100, 100))
tests.add(*generate_random_case(1000, 50))
tests.add(*generate_random_case(1000000, 5))
