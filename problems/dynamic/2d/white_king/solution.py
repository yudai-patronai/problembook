#!/usr/bin/env python3

def try_set(d, i, j):
    if 0 <= i <= 7 and 0 <= j <= 7:
        d[i][j] = -1


d = [[0] * 8 for i in range(8)]

s = input()
i = int(s[1]) - 1
j = ord(s[0]) - ord('a')
try_set(d, i, j)
try_set(d, i-2, j-1)
try_set(d, i-2, j+1)
try_set(d, i+2, j-1)
try_set(d, i+2, j+1)
try_set(d, i-1, j-2)
try_set(d, i-1, j+2)
try_set(d, i+1, j-2)
try_set(d, i+1, j+2)
d[0][0] = 1

if d[7][7]:
    print(0)
    exit()

for i in range(1, 8):
    if d[i][0] == -1:
        break
    d[i][0] = 1

for i in range(1, 8):
    if d[0][i] == -1:
        break
    d[0][i] = 1

for i in range(1, 8):
    for j in range(1, 8):
        if d[i][j] == -1:
            continue
        if d[i-1][j] != -1:
            d[i][j] += d[i-1][j]
        if d[i-1][j-1] != -1:
            d[i][j] += d[i-1][j-1]
        if d[i][j-1] != -1:
            d[i][j] += d[i][j-1]

print(d[7][7])
