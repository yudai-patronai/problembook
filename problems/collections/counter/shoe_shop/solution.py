from collections import Counter

X = input()
sizes = Counter(map(int, input().split()))
N = int(input())
money = 0
for i in range(N):
    s, m = map(int, input().split())
    if sizes[s] > 0:
        money += m
        sizes[s] -= 1
print(money)
