#!/usr/bin/python3


n = int(input())
m = int(input())

g = {x: set() for x in range(n)}

for i in range(m):
    f, t = map(int, input().split())
    g[f].add(t)
    g[t].add(f)

fired = set()

k = 0
while len(fired) < n:
    for i in range(n):
        if i not in fired:
            s = [i]
            break

    while s:
        v1 = s.pop(-1)
        fired.add(v1)
        for v2 in g[v1]:
            if v2 not in fired:
                s.append(v2)

    k += 1

print(k)
