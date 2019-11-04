from lib.testgen import TestSet

def question(A):
    return ' '.join(map(str, A)) + '\n'


def answer(A):
    return ' '.join(map(str, A)) + '\n'

def hoar_sort(A, depth=1, part='left', log=[]):
    log.append( 'depth: {} part: {} array before: {}'.format(depth, part, A))
    if len(A) <= 1:
        return

    barrier = A[0]

    L, M, R = [], [], []
    for elem in A:
        if elem < barrier:
            L.append(elem)
        elif elem == barrier:
            M.append(elem)
        else:
            R.append(elem)

    hoar_sort(L, depth + 1, 'left', log)
    hoar_sort(R, depth + 1, 'right', log)

    j = 0
    for elem in L + M + R:
        A[j] = elem
        j += 1
    log.append( 'depth: {} part: {} array after: {}'.format(depth, part, A))


tests = TestSet()

for arr in [2, 4, 8, 1, 2, 3, 10], [3, 4, 2, 0, 6, 6], [2, 4, 8], [10, 7, 4, 1, 8, 1, 12, 5, 7, 9, 4, 3, 2, 12, 2]:
    log = []
    q = question(arr)
    hoar_sort(arr, log=log)

    tests.add(
        q,
        '\n'.join(log) + '\n'
    )
