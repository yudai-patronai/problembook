a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] % 2 != 0:
        continue
    m = i
    for j in range(i+1, len(a)):
        if a[j] % 2 == 0 and a[m] > a[j]:
            m = j
    a[m], a[i] = a[i], a[m]

print(*a)
