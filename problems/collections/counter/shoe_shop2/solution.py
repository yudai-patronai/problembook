from collections import Counter

X = input()
sizes = Counter(map(int, input().split()))
N = int(input())

customers = []

for i in range(N):
    s, m = map(int, input().split())
    customers.append((m, s))

customers = sorted(customers, reverse=True)

money = 0
for m, s in customers:
    if sizes[s] > 0:
        money += m
        sizes[s] -= 1

print(money)
