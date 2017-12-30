#!/usr/bin/env python3

n = 0
s = 0
s_sq = 0
elem = int(input())
while elem != 0:
    n += 1
    s += elem
    s_sq += elem*elem
    elem = int(input())
mean = s / n
var = s_sq / n - mean * mean

print(round(mean, 3), round(var, 3))
