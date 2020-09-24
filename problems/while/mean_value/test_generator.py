from lib import random
from lib.testgen import TestSet

def join_all(arr):
    return '\n'.join(map(str, arr)) + '\n'

tests = TestSet()
random.seed(42)

n = 6

for num in range(n):
    if num == 1:
        seq = [random.randint(1, 10000)]

    elif num == 2:
        seq = [random.randint(1, 10000)] * 3
    
    elif num == 3:
        seq = [random.randint(1, 10000) for i in range(3)]
    
    else:
        cur_max_random = random.randint(100, 10000)
        seq = [random.randint(1, cur_max_random) for i in range(random.randint(10, 200))]

    mean = round(sum(seq) / len(seq), 2)
    seq.append(0)

    tests.add(join_all(seq), str(mean) + '\n')
