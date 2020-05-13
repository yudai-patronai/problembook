#!/usr/bin/env python3


def wave(field, i1, j1):
    field[i1][j1] = 0
    queue = [(i1, j1)]

    while queue:
        i, j = queue.pop(0)
        if i > 0 and field[i - 1][j] == -1:
            field[i - 1][j] = field[i][j] + 1
            queue.append((i - 1, j))

        if j > 0 and field[i][j - 1] == -1:
            field[i][j - 1] = field[i][j] + 1
            queue.append((i, j - 1))

        if i < len(field) - 1 and field[i + 1][j] == -1:
            field[i + 1][j] = field[i][j] + 1
            queue.append((i + 1, j))

        if j < len(field[i]) - 1 and field[i][j + 1] == -1:
            field[i][j + 1] = field[i][j] + 1
            queue.append((i, j + 1))

    return (i, j)


def read_field(n):
    field = []
    for i in range(n):
        field.append([-2 if c == 'X' else -1 for c in input()])

    return field


def read_field_from_array(arr):
    field = []
    for a in arr:
        field.append([-2 if c == 'X' else -1 for c in a])

    return field


def solve(i1, j1, i2, j2, field):
    wave(field, i1, j1)
    return 'INF' if field[i2][j2] < 0 else str(field[i2][j2])


if __name__ == "__main__":
    n, m = map(int, input().split())
    i1, j1 = map(int, input().split())
    i2, j2 = map(int, input().split())
    f = read_field(n)
    print(solve(i1, j1, i2, j2, f))
