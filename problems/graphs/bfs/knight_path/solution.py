#!/usr/bin/env python3
import bisect
import os
import sys

#######################
# Library
#######################
start = input()
end = input()


def add(cell, move):
    return chr(ord(cell[0]) + move[0]) + chr(ord(cell[1]) + move[1])


def correct(cell):
    return "a" <= cell[0] <= "h" and "1" <= cell[1] <= "8"


Moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]


if __name__ == "__main__":
    D = dict() # расстояния
    P = dict() # предки

    for x in "abcdefgh":
        for y in "12345678":
            D[x + y] = -1
            P[x + y] = None

    D[start] = 0
    Q = [start]
    Qstart = 0

    while Qstart < len(Q):
        u = Q[Qstart]
        Qstart += 1
        for move in Moves:
            v = add(u, move)
            if correct(v) and D[v] == -1:
                D[v] = D[u] + 1
                P[v] = u
                Q.append(v)
    Ans = []
    curr = end
    while curr is not None:
        Ans.append(curr)
        curr = P[curr]
    print("\n".join(Ans[::-1]))


