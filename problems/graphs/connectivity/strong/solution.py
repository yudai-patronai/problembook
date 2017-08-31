#!/usr/bin/python3


def dfs(g, i, f):
    f.add(i)
    for j in g[i]:
        if j not in f:
            dfs(g, j, f)


n = int(input())
m = int(input())

g1 = {x: set() for x in range(n)}
g2 = {x: set() for x in range(n)}

for i in range(m):
    f, t = map(int, input().split())
    g1[f].add(t)
    g2[t].add(f)

fired1 = set()
fired2 = set()

dfs(g1, 0, fired1)
dfs(g2, 0, fired2)

print("YES" if len(fired1) == len(fired2) == n else "NO")
