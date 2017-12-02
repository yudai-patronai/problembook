#!/usr/bin/env python3

def solve(n, temp):
    cur_max = 0
    cur_days = 0
    for i in range(n):
        if temp[i] > 0:
            cur_days += 1
        else:
            if cur_max < cur_days:
                cur_max = cur_days
            cur_days = 0

    if cur_max < cur_days:
        cur_max = cur_days

    return cur_max


if __name__ == "__main__":
    n = int(input())
    temp = list(map(int, input().split()))

    print(solve(n, temp))
