#!/usr/bin/env python3


def solve(n, k, seq):
    for _ in range(k):
        res = [int((seq[i - 1] + seq[i] + seq[(i + 1) % n]) / 3)
               for i in range(len(seq))]
        seq = res
    return ' '.join(map(str, seq))


if __name__ == "__main__":
    n, k = map(int, input().split())
    seq = list(map(int, input().split()))
    print(solve(n, k, seq))
