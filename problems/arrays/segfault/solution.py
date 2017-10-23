#!/usr/bin/env python3

def solve(n, memory):
    currInd = 0
    while 0 < currInd + memory[currInd] < n:
        currInd = currInd + memory[currInd]
    return currInd

if __name__ == "__main__":

    n = int(input())
    memory = [0]*n
    for i in range(n):
        memory[i] = int(input())
    print(solve(n, memory))
