n = int(input())
a = [int(input()) for _ in range(n)]

for i in range(n):
    if a[i] % 2 != 0:
        continue
    m = i
    for j in range(i+1, n):
        if a[j] % 2 == 0 and a[m] > a[j]:
            m = j
    a[m], a[i] = a[i], a[m]

print(*a)
