n = int(input())
a = [int(input()) for _ in range(n)]
b = [int(input()) for _ in range(n)]
for i in range(n):
    for j in range(n-i-1):
        if a[j] > a[j+1] or a[j] == a[j+1] and b[j] > b[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            b[j], b[j+1] = b[j+1], b[j]
print(*a)
print(*b)
