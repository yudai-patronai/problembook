import random
import sys

from lib.testgen import TestSet

tests = TestSet()

def solv(ids, ages, N):
    rq = list(zip(ids, ages, range(N)))
    rx = sorted(rq, key=lambda item: item[1] * 1000000 - item[2], reverse=True)
    return rx


for test_id in range(5):
    N = random.randrange(5)
    ids = list(range(1, N+1))
    ages = [random.randrange(20, 60, 3) for _ in range(N)]

    statement = str(N) + "\n"

    random.shuffle(ids)
    random.shuffle(ages)
    for i in range(N):
        statement += f"{ids[i]} {ages[i]}\n"

    rx = solv(ids, ages, N)

    answer = "\n".join(str(r[0]) for r in rx)
    
    tests.add(statement, answer)

for test_id in range(15):
    N = random.randrange(10, 100)
    ids = list(range(1, N+1))
    ages = [random.randrange(10, 50) for _ in range(N)]

    statement = str(N) + "\n"

    random.shuffle(ids)
    random.shuffle(ages)
    for i in range(N):
        statement += f"{ids[i]} {ages[i]}\n"

    rx = solv(ids, ages, N)

    answer = "\n".join(str(r[0]) for r in rx)
    
    tests.add(statement, answer)
    
for test_id in range(5):
    N = random.randrange(5000, 10000)
    ids = list(range(1, N+1))
    ages = [random.randrange(10, 50) for _ in range(N)]

    statement = str(N) + "\n"

    random.shuffle(ids)
    random.shuffle(ages)
    for i in range(N):
        statement += f"{ids[i]} {ages[i]}\n"

    rx = solv(ids, ages, N)

    answer = "\n".join(str(r[0]) for r in rx)
    
    tests.add(statement, answer)

