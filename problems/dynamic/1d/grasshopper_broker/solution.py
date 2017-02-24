#!/usr/bin/python3

startup_capital = int(input())
percents = list(map(int, input().split()))
n = len(percents)

max_money = [startup_capital, 0, startup_capital*percents[2]] + [-1]*(n-3)
for i in range(3, n):
    money = max(max_money[i-2], max_money[i-3])
    max_money[i] = money*(100+percents[i])/100        

print(max(max_money))
