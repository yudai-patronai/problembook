#!/usr/bin/env python3


def find_distance(first, second):
    matrix = [[0] * (len(second) + 1) for i in range(len(first) + 1)]
    for i in range(len(first) + 1):
        matrix[i][0] = i
    for j in range(len(second) + 1):
        matrix[0][j] = j

    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            matrix[i][j] = min(
                matrix[i][j - 1] + 1,
                matrix[i - 1][j] + 1,
                matrix[i - 1][j - 1] + (first[i - 1] != second[j - 1]))
    return matrix[-1][-1]


if __name__ == "__main__":
    first = input()
    second = input()
    print(find_distance(first, second))
