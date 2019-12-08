#!/usr/bin/env python3


def levenstein(first, second, insert_cost, remove_cost, replace_cost):
    matrix = [[0] * (len(second) + 1) for i in range(len(first) + 1)]
    for i in range(len(first) + 1):
        matrix[i][0] = i * remove_cost
    for j in range(len(second) + 1):
        matrix[0][j] = j * insert_cost

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if first[i-1] == second[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(
                    matrix[i][j - 1] + insert_cost,
                    matrix[i - 1][j] + remove_cost,
                    matrix[i - 1][j - 1] + replace_cost
                )
    return matrix[-1][-1]


insert, remove, replace = map(int, input().split())

first = input()
second = input()

print(levenstein(first, second, insert, remove, replace))
