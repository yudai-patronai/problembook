#!/usr/bin/env python3

def solve(N, M):
    Answer = 0
    for i in range(N):
        if M[i] == "1":
            mind = 0
            while M[min(N - 1, i + mind)] != "2" and M[max(0, i - mind)] != "2":
                mind += 1
            Answer = max(Answer, mind)
    return (Answer)


if __name__ == "__main__":
    print(solve(int(input()), input().split()))
