#!/usr/bin/env python3
from queue import Queue


def generate_moves(num):
    moves = []
    if num % 10 > 1:
        moves.append(num-1)
    if num // 1000 < 9:
        moves.append(num+1000)
    moves.append(num % 1000 * 10 + num // 1000)
    moves.append(num // 10 + num % 10 * 1000)
    return moves


def restore_answer(f, u):
    if u == -1:
        return
    restore_answer(f, f[u])
    print(u)


if __name__ == "__main__":
    s = int(input())
    t = int(input())
    d = {}
    f = {}
    for i in range(1, 10):
        for j in range(1, 10):
            for k in range(1, 10):
                for l in range(1, 10):
                    d[i*1000 + j*100 + k*10 + l] = -1
                    f[i*1000 + j*100 + k*10 + l] = -1
    d[s] = 0
    q = Queue()
    q.put(s)
    while not q.empty():
        u = q.get()
        for v in generate_moves(u):
            if d[v] == -1:
                d[v] = d[u] + 1
                f[v] = u
                q.put(v)

    restore_answer(f, t)
