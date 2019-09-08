#!/usr/bin/env python3


def solve(n, heights):
    cost = [-1] * n
    cost[0] = 0
    if 1 == n:
        return 0
    cost[1] = abs(heights[1] - heights[0])
    for i in range(2, n):
        fromFirst = abs(heights[i] - heights[i - 1]) + cost[i - 1]
        fromSecond = 3 * abs(heights[i] - heights[i - 2]) + cost[i - 2]
        cost[i] = fromFirst if fromFirst < fromSecond else fromSecond
    return cost[n - 1]


if __name__ == "__main__":
    n = int(input())

    heights = []
    for _ in range(n):
        heights.append(int(input()))

    print(solve(n, heights))
