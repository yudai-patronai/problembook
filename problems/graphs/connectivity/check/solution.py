#!/usr/bin/python3


n = int(input())
m = int(input())

g = {x: set() for x in range(n)}

for i in range(m):
    f, t = map(int, input().split())
    g[f].add(t)
    g[t].add(f)

fired = set()

s = [0]

while s:
    v1 = s.pop(-1)
    fired.add(v1)
    for v2 in g[v1]:
        if v2 not in fired:
            s.append(v2)

print('YES' if len(fired) == n else 'NO')