from lib.testgen import TestSet

def cycle_solution(n):
    s = ''
    for i in range(n, 1, -1):
        s += 'verh matryoshki {}\n'.format(i)
    s += 'matryoshechka\n'
    for i in range(2, n+1):
        s += 'niz matryoshki {}\n'.format(i)

    return s

def question(n):
    return '{}\n'.format(n)

def answer(n):
    return cycle_solution(n)



tests = TestSet()
for i in [3, 8, 12, 50]:
    tests.add(question(i), answer(i))
