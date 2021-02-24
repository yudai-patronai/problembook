from lib.testgen import TestSet
from lib.random import seed, randint

seed(142)

RANDOM_TESTS = 9


def to_str(array):
    return ' '.join(map(str, array))

def question(french, swim, piano):
    return to_str(french) + '\n' + to_str(swim) + '\n' + to_str(piano) + '\n'

def answer(array):
    return to_str(array) + '\n'

def random_array(size=25, a=50, b=75):
    # list(set()) avoids repetitions
    return list(set([randint(a, b) for _ in range(size)]))


tests = TestSet()

# manual tests
tests.add(
    question(
        [1, 2, 5, 7, 8, 9],
        [3, 4, 8, 2, 10],
        [10, 3, 2, 8, 5]
    ),
    answer([3, 10])
)

for _ in range(RANDOM_TESTS):
    french = random_array(randint(5, 10))
    swim = random_array(randint(5, 15))
    piano = random_array(randint(5, 20))
    ans = sorted((set(swim) & set(piano)) - set(french))
    tests.add(
        question(french, swim, piano),
        answer(ans)
    )
