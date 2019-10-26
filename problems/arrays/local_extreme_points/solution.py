#!/usr/bin/python3

N = int(input())
x = [float(el) for el in input().split()]


def extreme_points(N, x):
    assert N == len(x)

    if N == 1 or N == 2:
        return ''

    buf = []
    for i in range(1, N-1):
        if x[i-1] > x[i] < x[i+1] or x[i-1] < x[i] > x[i+1]:
            buf.append(i)

    return ' '.join(map(str, buf))

print(extreme_points(N, x))

