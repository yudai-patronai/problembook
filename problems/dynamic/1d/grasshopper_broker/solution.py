#!/usr/bin/python3

startup_capital = int(input())
percents = list(map(int, input().split()))
n = len(percents)

max_money = [startup_capital, 0,
             startup_capital * (1 + percents[2] / 100)] + [-1] * (n - 3)
for i in range(3, n):
    money = max(max_money[i - 2], max_money[i - 3])
    max_money[i] = money * (1 + percents[i] / 100)

i, m = max(enumerate(max_money), key=lambda x: x[1])

path = []

while i != 0:
    path.append(i + 1)
    k = 2 if max_money[i - 2] * (1 + percents[i] / 100) == m else 3
    m = max_money[i - k]
    i -= k

print(1, *reversed(path))
