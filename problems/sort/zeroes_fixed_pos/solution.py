#!/usr/bin/python3

l = list(map(int, input().split()))


def slow(l):
    n = len(l)

    for i in range(n - 1):
        if l[i] == 0:
            continue
        m = i
        for j in range(i, n):
            if l[j] == 0:
                continue
            if l[j] < l[m]:
                m = j
        if m != i:
            l[i], l[m] = l[m], l[i]

    return l


def fast(l):
    zeroes_positions = [i for i, x in enumerate(l) if x == 0]
    non_zeroes = sorted(x for x in l if x != 0)

    zeroes_positions.append(len(l))
    cz = 0
    cnz = 0
    for i in range(len(l)):
        if i < zeroes_positions[cz]:
            yield non_zeroes[cnz]
            cnz += 1
        else:
            yield 0
            cz += 1


print(' '.join(map(str, fast(l))))
