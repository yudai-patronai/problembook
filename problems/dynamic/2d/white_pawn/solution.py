#!/usr/bin/env python3

d = [[0] * 8 for i in range(8)]
n = int(input())
for i in range(n):
    s = input()
    d[int(s[1]) - 1][ord(s[0]) - ord('a')] = 1


s = input()
i0 = int(s[1]) - 1
j0 = ord(s[0]) - ord('a')
for j in range(8):
    d[i0][j] = 0
d[i0][j0] = 1


for i in range(i0 + 1, 8):
    for j in range(8):
        if d[i][j] == 1:
            d[i][j] = 0
            if j > 0:
                d[i][j] += d[i - 1][j - 1]
            if j < 7:
                d[i][j] += d[i - 1][j + 1]
        else:
            d[i][j] = d[i - 1][j]

s = 0
for i in range(8):
    s += d[7][i]

print(s)
