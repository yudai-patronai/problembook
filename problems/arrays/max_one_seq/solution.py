#!/usr/bin/env python3
def solve(N, arr):
    max_seq = 0
    cur_seq = 0
    for i in range(N):
        if arr[i] == 0:
            if cur_seq > max_seq:
                max_seq = cur_seq
            cur_seq = 0
        else:
            cur_seq += 1

    if cur_seq > max_seq:
        max_seq = cur_seq
    return max_seq

if __name__ == "__main__":
    N = int(input())
    arr = [0] * N
    for i in range(N):
        arr[i] = int(input())
    print(solve(N, arr))
