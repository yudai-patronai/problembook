#!/usr/bin/env python3

from lib.graphs import task


def floyd(dist):
    n = len(dist)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])


def solve(matrix):
    floyd(matrix)

    sums = [sum(a) for a in matrix]

    return '%d\n' % sums.index(min(sums))


if __name__ == "__main__":
    n, m, matrix = task.read_task_weight_adj_matrix()
    print(solve(matrix), end='')
