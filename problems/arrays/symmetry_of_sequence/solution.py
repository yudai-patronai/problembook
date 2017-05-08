#!/usr/bin/env python3


def solve(n, seq):
    for i in range(len(seq)):
        toAdd = seq[:i][::-1]
        newseq = seq + toAdd
        if newseq == newseq[::-1]:
            return str(i) + '\n' + ' '.join(map(str, toAdd))


if __name__ == "__main__":
    print(solve(int(input()), list(map(int, input().split()))))
